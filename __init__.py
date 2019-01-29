from flask import request, render_template
from functools import wraps
from .config import config
import logging
import requests
import json
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.DEBUG)

def load(app):
    config(app)

    def register_decorator(register_func):
        @wraps(register_func)
        def wrapper(*args, **kwargs):
            if request.method == 'POST':
                errors = []
                bad_request = False
                
                params = {
                    'name' : request.form['name'],
                    'password' : request.form['password'],
                    'roles' : app.config['SPLUNK_ROLE']
                }
                
                # Consider an if statement here to check if user exists in Splunk yet

                creds = HTTPBasicAuth(app.config['SPLUNK_USERNAME'], app.config['SPLUNK_PASSWORD'])
                
                request_url = app.config['SPLUNK_SERVER'] + '/services/authentication/users'
                
                verify_response = requests.post(request_url, data=params, auth=creds, verify=False)
                logging.debug("Attempting to create User on Splunk server: {}".format(request_url))
                
                if not verify_response.ok:
                    bad_request = True
                    logging.debug("Got an error from the Splunk server.")

                if bad_request:
                    errors.append("Unable to contact Splunk server to create your account.")
                else:
                    return register_func(*args, **kwargs)

                return render_template(
                    'register.html',
                    errors=errors,
                    name=request.form['name'],
                    email=request.form['email'],
                    password=request.form['password']
                )
            else:
                return register_func(*args, **kwargs)

        return wrapper

    app.view_functions['auth.register'] = register_decorator(app.view_functions['auth.register'])
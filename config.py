def config(app):
    app.config['SPLUNK_SERVER'] = 'https://x.x.x.x:8089'
    app.config['SPLUNK_USERNAME'] = 'user'
    app.config['SPLUNK_PASSWORD'] = 'password'
    app.config['SPLUNK_ROLE'] = 'role'


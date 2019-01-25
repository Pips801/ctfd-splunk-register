def config(app):
    app.config['SPLUNK_SERVER'] = 'https://35.247.124.251:8089'
    app.config['SPLUNK_USERNAME'] = 'ctfd'
    app.config['SPLUNK_PASSWORD'] = 'p4ssw0rd1'
    app.config['SPLUNK_ROLE'] = 'admin'


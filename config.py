def config(app):
    app.config['SPLUNK_SERVER'] = 'http://localhost:1234'
    app.config['SPLUNK_USERNAME'] = 'admin'
    app.config['SPLUNK_PASSWORD'] = 'pw'
    app.config['SPLUNK_ROLE'] = 'user'


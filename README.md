# ctfd-splunk-register

A plugin for CTFd to create a Splunk account at the same time as the user registers for CTFd, with the same password.
This uses the Splunk API endpoint, running on port 8089.

# Install

1. Deploy CTFd
2. ```git clone https://github.com/Pips801/ctfd-splunk-register CTFd/CTFd/plugins/ctfd-splunk-register```
3. Edit settings.py and put in your Splunk server IP/port, username, password, and role for new users to be put in.

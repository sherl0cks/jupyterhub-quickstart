import os

c.Authenticator.admin_users = {'jholmes'}
c.Authenticator.whitelist = {'jholmes','obedin','jholmes-tester','djurgens'}
c.LocalAuthenticator.create_system_users = True
c.JupyterHub.authenticator_class = 'oauthenticator.openshift.OpenShiftOAuthenticator'
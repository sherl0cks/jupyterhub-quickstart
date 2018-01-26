import os

c.Authenticator.admin_users = {'jholmes'}
c.Authenticator.whitelist = {'jholmes','foo'}
c.LocalAuthenticator.create_system_users = True
c.JupyterHub.authenticator_class = 'jupyterhub.auth.LocalAuthenticator'
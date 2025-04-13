import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #DB_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
    #DB_URI = 'sqlite:///{}'.format(DB_PATH)

    CLIENT_ID = '1073998933994-jbgtdgdm74jr4aptmj74v56gvotppmkq.apps.googleusercontent.com'
    CLIENT_SECRET = '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'
    REDIRECT_URI = 'https://localhost:8080/oauth/callback'  # Should match your Google settings
    AUTHORIZATION_BASE_URL = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
    SCOPE = ['https://www.googleapis.com/auth/userinfo.email','https://www.googleapis.com/auth/userinfo.profile']
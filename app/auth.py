from flask import Flask, redirect, request, url_for, session
from requests_oauthlib import OAuth2Session
import os

# Configuration
client_id = 'input_id_here'
client_secret = 'input_secret_here'
redirect_uri = 'https://localhost:8080/callback'  # Should match your Google settings
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'
scope = ['https://www.googleapis.com/auth/userinfo.email']

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Random secret key for session management

@app.route('/')
def home():
    return '<a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = oauth.authorization_url(authorization_base_url)
    session['oauth_state'] = state  # Store state in session
    print(session['oauth_state'])
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    oauth = OAuth2Session(client_id, state=session.get('oauth_state'), redirect_uri=redirect_uri)
    token = oauth.fetch_token(token_url, authorization_response=request.url, client_secret=client_secret)
    session['oauth_token'] = token  # Store token in session
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    oauth = OAuth2Session(client_id, token=session['oauth_token'])
    user_info = oauth.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    print(user_info)
    return f'Hello, {user_info["email"]}!'


@app.route('/logout')
def logout():
    session.pop('oauth_token', None)  # Remove token from session
    return 'You have been logged out! <a href="/">Return to home</a>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=8080, ssl_context=('static/ssl_key/cert.pem', 'static/ssl_key/key.pem'))
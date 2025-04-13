import flask_login
from flask import Flask, redirect, request, url_for, session,current_app, flash
from flask_login import LoginManager, login_user,login_required, logout_user
from requests_oauthlib import OAuth2Session
from . import oauth
from model.models import *
import os




# Configuration

print("config in auth bp",current_app.config)
client_id = current_app.config['CLIENT_ID']
client_secret = current_app.config['CLIENT_SECRET']
redirect_uri = current_app.config['REDIRECT_URI']  # Should match your Google settings
authorization_base_url = current_app.config['AUTHORIZATION_BASE_URL']
token_url = current_app.config['TOKEN_URL']
scope = current_app.config['SCOPE']

print("ALL",client_secret,redirect_uri,authorization_base_url,token_url,scope)


@oauth.route('/login')
def login():
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = oauth.authorization_url(authorization_base_url)
    session['oauth_state'] = state  # Store state in session
    print("oauth login",session['oauth_state'])
    return redirect(authorization_url)

@oauth.route('/callback')
def callback():
    print("callback")
    oauth = OAuth2Session(client_id, state=session.get('oauth_state'), redirect_uri=redirect_uri)
    token = oauth.fetch_token(token_url, authorization_response=request.url, client_secret=client_secret)
    session['oauth_token'] = token  # Store token in session
    return redirect(url_for('oauth.profile'))

@oauth.route('/profile')
def profile():
    oauth = OAuth2Session(client_id, token=session['oauth_token'])
    print(session['oauth_token'])
    user_info = oauth.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    user_email = str(user_info["email"])
    user_id = str(user_info["id"])
    user_name = str(user_info["name"])

    user = USER_INFO.query.filter_by(email=user_email).first()

    if user is not None and user.group_id == 1:
        login_user(user)
        flash('login successfully')
        print(session)
        return redirect(url_for('main.index'))
    else:
        add_new_user = USER_INFO(user_name=user_name, email=user_email,group_id=1)
        db.session.add(add_new_user)
        db.session.commit()
        login_user(user)
        flash('welcome new comer! login successfully')
        print(session)
        return redirect(url_for('main.index'))




    #return f'Hello, {user_info["name"]},{user_info["email"]}!'




@oauth.route('/logout')
def logout():
    session.pop('oauth_token', None)  # Remove token from session

    return 'You have been logged out! <a href="/">Return to home</a>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=8080, ssl_context=('../static/ssl_key/cert.pem', '../static/ssl_key/key.pem'))
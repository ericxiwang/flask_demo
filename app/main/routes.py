from app.main import main
from flask import render_template,flash, request,session, redirect,url_for
from model.models import *
import os,json,uuid

@main.route('/',methods=['POST', 'GET'])

def login():
    if request.method == 'POST':
        email = request.form['email']
        user_password = request.form['user_password']
        user = USER_INFO.query.filter_by(email=email).first()
        if user is not None and user_password == user.user_password:
            #login_user(user, remember=id)
            flash('login successfully')
            #print(session['_id'])
            return redirect(url_for('main.index'))
        flash('wront login info')
    return render_template('login.html')

@main.route('/index')
def index():
    return render_template('index.html')
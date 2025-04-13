from app.main import main
from flask import render_template,flash, request,session, redirect,url_for,current_app
from model.models import *
from flask_login import login_user,login_required, logout_user
import os,json,uuid

@main.route('/',methods=['POST', 'GET'])

def login():
    if request.method == 'POST':
        email = request.form['email']
        user_password = request.form['user_password']
        user = USER_INFO.query.filter_by(email=email).first()
        if user is not None and user_password == user.user_password:
            login_user(user)
            flash('login successfully')
            print(session)
            return redirect(url_for('main.index'))
        flash('wront login info')
    return render_template('login.html')

@main.route('/index')
@login_required
def index():
    return render_template('index.html')


@main.route('/data_grid', methods=['GET'])
@login_required
def data_grid():
    new_grid_list = []
    all_albums_info = IMAGE_ALBUM.query.all()
    for each_line in all_albums_info:
        new_grid = {}
        new_grid["id"] = each_line.id
        new_grid["name"] = each_line.album_name
        new_grid["description"] = each_line.album_description
        new_grid["count"] = IMAGE_INFO.query.filter_by(img_album=each_line.album_name).count()
        new_grid_list.append(new_grid)
    print(new_grid_list)

    return render_template('data_grid.html', all_albums_info=new_grid_list)


@main.route('/logout')
@login_required
def logout():

    logout_user()
    return render_template('login.html')
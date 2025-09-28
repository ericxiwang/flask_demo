# -*- coding: utf-8 -*-
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()


class USER_INFO(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    user_password = db.Column(db.String(150), unique=False)
    group_id = db.Column(db.String(20),unique=False)

class USER_GROUP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), unique=False, nullable=False)


class IMAGE_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_uuid = db.Column(db.String(150), unique=False, nullable=False)
    img_description = db.Column(db.String(50), unique=False, nullable=False)
    img_album = db.Column(db.String(150), unique=False, nullable=False)


class IMAGE_ALBUM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(100), unique=False, nullable=False)
    album_description = db.Column(db.String(100), unique=False, nullable=False)
    __table_args__ = (db.UniqueConstraint('id', 'album_name'),)


class PRODUCT_CATEGORY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=False, nullable=False)
    category_desc = db.Column(db.String(150), unique=False, nullable=False)
class BUG_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bug_title = db.Column(db.String(50), unique=False, nullable=False)
    bug_desc = db.Column(db.String(150), unique=False, nullable=False)
    bug_level = db.Column(db.Integer, unique=False, nullable=False)
    bug_assignee = db.Column(db.String(150), unique=False, nullable=False)
    bug_status = db.Column(db.String(150), unique=False, nullable=False)
    bug_category = db.Column(db.String(150), unique=False, nullable=False)
    bug_keywords = db.Column(db.String(150), unique=False, nullable=False)
    bug_datatime = db.Column(db.String(150), unique=False, nullable=False)
    bug_project = db.Column(db.Integer, unique=False, nullable=False)

class TICKET_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_title = db.Column(db.String(50), unique=False, nullable=False)
    ticket_type = db.Column(db.String(150), unique=False, nullable=False)
    ticket_description = db.Column(db.String(150), unique=False, nullable=False)
    ticket_submitter = db.Column(db.String(150), unique=False, nullable=False)
    ticket_datetime = db.Column(db.String(150), unique=False, nullable=False)
    ticket_assignee = db.Column(db.String(150), unique=False, nullable=False)
    ticket_status = db.Column(db.String(150), unique=False, nullable=False)
    ticket_scope = db.Column(db.String(150), unique=False, nullable=False)

class PROJECT_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), unique=False, nullable=False)
    project_desc = db.Column(db.String(150), unique=False, nullable=False)
    project_owner = db.Column(db.String(50), unique=False, nullable=False)


if __name__ == "__main__":
    print(os.path)
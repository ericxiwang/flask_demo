from flask import request,jsonify,stream_with_context,Response
from app.api import flask_api
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import json,time
from model.models import *
@flask_api.route('/user_ops/<string:method>',methods=['POST','GET'])

def user_ops(method):
    if method == "new":
        if request.method == "POST":
            data = json.loads(request.data)
            new_user_record = USER_INFO(user_name=data['user_name'],
                                        user_password=data['user_password'],
                                        email=data['email'],
                                        group_id=data['group_id']
                                        )
            db.session.add(new_user_record)
            db.session.commit()
        return jsonify(data)
    elif method == "delete":
        if request.method == "POST":
            user_to_del = json.loads(request.data)
            print(user_to_del)
            user_to_delete = USER_INFO.query.get(user_to_del['id'])
            db.session.delete(user_to_delete)
            db.session.commit()
        return jsonify({"user": user_to_del['id']})

    elif method == "update":
        if request.method == "POST":
            data = json.loads(request.data)
            selected_user = USER_INFO.query.filter_by(id=data['id']).first()
            selected_user.user_name = data['user_name']
            selected_user.email = data['email']
            selected_user.group_id = data['group_id']
            db.session.commit()
            return jsonify(data)


    elif method == "all":
        all_users = USER_INFO.query.all()
        user_list = [each_user.to_dict() for each_user in all_users]


        return jsonify(user_list)

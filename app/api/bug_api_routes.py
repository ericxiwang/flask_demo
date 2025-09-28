from flask import request,jsonify,stream_with_context,Response
from app.api import flask_api
#from .algorithms import *
from .bug_operation import *

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import json,time
from model.models import *
@flask_api.route('/project_info',methods=['GET'])

def project_list():
    project_return = []
    project_info = PROJECT_INFO.query.all()
    for each_project in project_info:
        each_append = {'project_id': each_project.id, 'project_name': each_project.project_name}
        project_return.append(each_append)
    return jsonify(project_return)


@flask_api.route('/b_dashboard_main',methods=['POST'])

def b_bashboard_query():
    if request.method == "POST" and request.is_json:
        project_list = request.get_json()['key_words']
        dashboard_list_object = []

        bug_dashboard_list = BUG_INFO.query.filter(BUG_INFO.bug_project.in_(project_list)).all()
        for each_item in bug_dashboard_list:
            each_bug = {"bug_id":each_item.id,
                        "bug_title":each_item.bug_title,
                        "bug_desc": each_item.bug_desc,
                        "bug_level": each_item.bug_level,
                        "bug_assignee": each_item.bug_assignee,
                        "bug_status": each_item.bug_status,
                        "bug_category": each_item.bug_category,
                        "bug_project": each_item.bug_project,

                        }
            dashboard_list_object.append(each_bug)
        print("return bug list",dashboard_list_object)




    return jsonify(dashboard_list_object)

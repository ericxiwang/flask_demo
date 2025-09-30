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

def b_dashboard_query():
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



@flask_api.route('/b_dashboard_ops/<string:method>',methods=['POST'])
def b_dashboard_ops(method):

    if method == "new":
        if request.is_json:
            data = request.get_json()
            print(data['bug_title'])

            current_new_record = BUG_INFO(bug_title=data['bug_title'],
                                          bug_desc=data['bug_desc'],
                                          bug_status=data['bug_status'],
                                          bug_assignee=data['bug_assignee'],
                                          bug_level=data['bug_level'],
                                          bug_category=data['bug_category'],
                                          bug_datetime=data['bug_datetime'],
                                          bug_project=data['bug_project'])
            db.session.add(current_new_record)
            db.session.commit()
            return jsonify(data)
    elif method == "edit":

        print("update bug ticket info")
        if request.is_json:
            data = request.get_json()

            query_from_db = BUG_INFO.query.filter_by(id=int(data['ticket_id'])).first()
            query_from_db.ticket_title = data['ticket_title']
            query_from_db.ticket_description = data['ticket_desc']
            query_from_db.ticket_status = data['ticket_status']
            query_from_db.ticket_type = data['ticket_type']
            query_from_db.ticket_submitter = data['ticket_submitter']

            db.session.commit()
            return jsonify(data)


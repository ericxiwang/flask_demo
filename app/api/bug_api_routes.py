from flask import request,jsonify,stream_with_context,Response
from app.api import flask_api
#from .algorithms import *
from .bug_operation import *

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import json,time
from model.models import *
@flask_api.route('/',methods=['POST'])
@jwt_required()
def index():
    return "api---1"

@flask_api.route('/test/',methods=['POST'])
def categories():
    hash_map = {"name":"Eric", "age": 999, "summary": "this is test api"}
    return_test_value = jsonify(hash_map)
    return return_test_value


@flask_api.route('/a_dashboard_main/',methods=['POST'])
def a_dashboard_main_datagrid():
    NewTickets = []
    InProgressTickets = []
    ReviewTickets = []
    DoneTickets = []
    AllTickets = {"NewTickets":NewTickets,
                  "InProgressTickets":InProgressTickets,
                  "ReviewTickets":ReviewTickets,
                  "DoneTickets":DoneTickets
                  }
    all_tickets = TICKET_INFO.query.all()
    for each_ticket in all_tickets:
        candidate_ticket = {"id": each_ticket.id,
                            "title": each_ticket.ticket_title,
                            "type": each_ticket.ticket_type,
                            "desc": each_ticket.ticket_description,
                            "submitter": each_ticket.ticket_submitter,
                            "status": each_ticket.ticket_status,
                            "assignee": each_ticket.ticket_assignee}

        if  candidate_ticket["status"] == "new":
            NewTickets.append(candidate_ticket)
        elif candidate_ticket["status"] == "inprogress":
            InProgressTickets.append(candidate_ticket)
        elif candidate_ticket["status"] == "review":
            ReviewTickets.append(candidate_ticket)
        elif candidate_ticket["status"] == "done":
            DoneTickets.append(candidate_ticket)
        else:
            pass





    return jsonify(AllTickets)

@flask_api.route('/a_dashboard_ops/<string:method>',methods=['POST'])
def a_dashboard_edit(method):

    if method == "new":
        if request.is_json:
            data = request.get_json()
            print(data['title'])

            current_new_record = TICKET_INFO(ticket_title=data['title'],
                                             ticket_description=data['desc'],
                                             ticket_status=data['status'],
                                             ticket_assignee=data['submitter'],
                                             ticket_type=data['type'],
                                             ticket_submitter=data['submitter'])
            db.session.add(current_new_record)
            db.session.commit()
            return jsonify(data)
    elif method == "edit":

        print("update ticket info")
        if request.is_json:
            data = request.get_json()

            query_from_db = TICKET_INFO.query.filter_by(id=int(data['id'])).first()
            query_from_db.ticket_title = data['title']
            query_from_db.ticket_description = data['desc']
            query_from_db.ticket_status = data['status']
            query_from_db.ticket_submitter = data['submitter']

            db.session.commit()
            return jsonify(data)











@flask_api.route('/product_cate_list/<string:method>',methods=['POST'])
def product_cate_edit(method):
    print(method)


    if method == "query":
        cate_list = []
        all_categories = BUG_INFO.query.all()
        for each_line in all_categories:
            new_grid = {}
            new_grid["id"] = each_line.id
            new_grid["bug_title"] = each_line.bug_title
            new_grid["bug_desc"] = each_line.bug_desc
            cate_list.append(new_grid)
        print(cate_list)



        return jsonify(cate_list)
    elif method == "add":
        if request.is_json:
            data = request.json['new_cate']
            print(data)
            for each_line in data:
                print(each_line)
                name = each_line['name']
                description = each_line['description']
                current_new_record = PRODUCT_CATEGORY(category_name=name,category_desc=description)
                db.session.add(current_new_record)
                db.session.commit()


                return jsonify("add item successfully")
        else:
            return jsonify("add item failed")



@flask_api.route('/sse')
def sse_events():
    def generate_events():
        while True:
            # Simulate real-time data
            current_time = time.strftime("%H:%M:%S")
            data = {"time": current_time, "message": "Hello from Flask BackEnd SSE!"}
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(1) # Send an event every second

    return Response(stream_with_context(generate_events()), mimetype='text/event-stream')



@flask_api.route('/auth', methods=['POST'])
def api_auth():
    data = json.loads(request.data)
    if request.method == 'POST':
        user_name = data['user_name']
        user_password = data['user_password']
        user = "admin@admin.com"

        if user is not None and user_password == "1234":
            access_token = create_access_token(identity=user_name)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"message": "can not found user, auth failed"})
    else:
        help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
        return json.dumps(help_info)
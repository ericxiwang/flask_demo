from flask import request,jsonify,stream_with_context,Response
from app.api import flask_api
#from .algorithms import *
from .bug_operation import *

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import json,time
from model.models import *
@flask_api.route('/',methods=['POST'])
def index():
    return "api---1"
@flask_api.route('/auth', methods=['POST'])
def api_auth():


    if request.method == 'POST':
        data = request.get_json()


        email = data.get('email').strip()
        user_password = data.get('user_password').strip()


        if email and user_password:
            get_current_user_password = USER_INFO.query.filter_by(email=email).first()

            if get_current_user_password and get_current_user_password.user_password == user_password:

                access_token = create_access_token(identity=email)
                return jsonify(access_token=access_token), 200
            else:
                return jsonify({"message": "wrong username or password"})
        else:
            return jsonify({"message": "input can not be empty"})
    else:
        help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
        return json.dumps(help_info)





@flask_api.route('/test',methods=['POST'])
def categories():
    hash_map = {"name":"Eric", "age": 999, "summary": "this is test api"}
    return_test_value = jsonify(hash_map)
    return return_test_value


@flask_api.route('/a_dashboard_main',methods=['POST','OPTIONS'])

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
        candidate_ticket = {"ticket_id": each_ticket.id,
                            "ticket_title": each_ticket.ticket_title,
                            "ticket_type": each_ticket.ticket_type,
                            "ticket_desc": each_ticket.ticket_description,
                            "ticket_submitter": each_ticket.ticket_submitter,
                            "ticket_datetime": each_ticket.ticket_datetime,
                            "ticket_status": each_ticket.ticket_status,
                            "ticket_assignee": each_ticket.ticket_assignee}

        if  candidate_ticket["ticket_status"] == "new":
            NewTickets.append(candidate_ticket)
        elif candidate_ticket["ticket_status"] == "inprogress":
            InProgressTickets.append(candidate_ticket)
        elif candidate_ticket["ticket_status"] == "review":
            ReviewTickets.append(candidate_ticket)
        elif candidate_ticket["ticket_status"] == "done":
            DoneTickets.append(candidate_ticket)
        else:
            pass





    return jsonify(AllTickets)
@flask_api.route('/a_workflow_ticketlist/<string:current_user>',methods=['GET'])

def a_workflow_ticketlist(current_user):
    return_list = []

    if request.method == "GET":
        if current_user != 'all':


            all_selected_tickets = TICKET_INFO.query.filter_by(ticket_assignee=current_user).all()


        elif current_user == 'all':
            all_selected_tickets = TICKET_INFO.query.all()
        else:
            pass

        for each_ticket in all_selected_tickets:
            candidate_ticket = {"id": each_ticket.id,
                                "title": each_ticket.ticket_title,
                                "type": each_ticket.ticket_type,
                                "desc": each_ticket.ticket_description,
                                "submitter": each_ticket.ticket_submitter,
                                "status": each_ticket.ticket_status,
                                "assignee": each_ticket.ticket_assignee}
            return_list.append(candidate_ticket)

    return jsonify(return_list)
@flask_api.route('/a_dashboard_ops/<string:method>',methods=['POST'])
def a_dashboard_edit(method):

    if method == "new":
        if request.is_json:
            data = request.get_json()
            print(data['ticket_title'])

            current_new_record = TICKET_INFO(ticket_title=data['ticket_title'],
                                             ticket_description=data['ticket_desc'],
                                             ticket_status=data['ticket_status'],
                                             ticket_assignee=data['ticket_assignee'],
                                             ticket_type=data['ticket_type'],
                                             ticket_submitter=data['ticket_submitter'],
                                             ticket_datetime=data['ticket_datetime'])
            db.session.add(current_new_record)
            db.session.commit()
            print(current_new_record.id)

            return jsonify({"ticket_id":current_new_record.id})
    elif method == "edit":

        print("update ticket info")
        if request.is_json:
            data = request.get_json()

            query_from_db = TICKET_INFO.query.filter_by(id=int(data['ticket_id'])).first()
            query_from_db.ticket_title = data['ticket_title']
            query_from_db.ticket_description = data['ticket_desc']
            query_from_db.ticket_status = data['ticket_status']
            query_from_db.ticket_type = data['ticket_type']
            query_from_db.ticket_submitter = data['ticket_submitter']

            db.session.commit()
            return jsonify(query_from_db.id)
    elif method == "delete":

        print("delete current ticket")
        if request.is_json:
            data = request.get_json()

            query_from_db = TICKET_INFO.query.filter_by(id=int(data['ticket_id'])).first()

            db.session.delete(query_from_db)
            db.session.commit()
            return jsonify(query_from_db.id)




@flask_api.route('/a_workflow_badge',methods=['POST'])
def a_workflow_badge():

    new_tickets = TICKET_INFO.query.filter_by(ticket_status='new').count()
    inprogress_tickets = TICKET_INFO.query.filter_by(ticket_status='inprogress').count()
    review_tickets = TICKET_INFO.query.filter_by(ticket_status='review').count()
    done_tickets = TICKET_INFO.query.filter_by(ticket_status='done').count()

    AllTickets = {"NewTickets": new_tickets,
                  "InProgressTickets": inprogress_tickets,
                  "ReviewTickets": review_tickets,
                  "DoneTickets": done_tickets
                  }



    return jsonify(AllTickets)


@flask_api.route('/all_user',methods=['POST','GET'])
def all_user():
    user_list = []
    all_users = USER_INFO.query.all()
    for each_line in all_users:
        each_user = {}
        each_user["id"] = each_line.id
        each_user["user_name"] = each_line.user_name
        each_user["email"] = each_line.email
        each_user["group_id"] = each_line.group_id
        user_list.append(each_user)
    print(user_list)
    return jsonify(user_list)





###################################### project management #######################


@flask_api.route('/project_list/<string:method>',methods=['POST'])
def project_management(method):
    print(method)

    if method == "query":
        project_list = []
        all_projects = PROJECT_INFO.query.all()
        for each_line in all_projects:
            new_grid = {}
            new_grid["id"] = each_line.id
            new_grid["project_name"] = each_line.project_name
            new_grid["project_desc"] = each_line.project_desc
            new_grid["project_owner"] = each_line.project_owner
            project_list.append(new_grid)

        return jsonify(project_list)
    elif method == "add":
        if request.method == "POST":
            data = json.loads(request.data)
            new_project = PROJECT_INFO(project_name=data['project_name'],project_desc=data['project_desc'],project_owner=data['project_owner'])
            db.session.add(new_project)
            db.session.commit()

            return jsonify({"new_project_id": new_project.id})

    elif method == "edit":
        if request.method == "POST":
            data = json.loads(request.data)
            edit_project = PROJECT_INFO.query.filter_by(id=int(data['project_id'])).first()
            edit_project.project_name = data["project_name"]
            edit_project.project_desc = data["project_desc"]
            edit_project.project_owner = data["project_owner"]
            db.session.add(edit_project)
            db.session.commit()

            return jsonify(edit_project.to_dict())

    elif method == "delete":
        if request.method == "POST":
            project_id = json.loads(request.data)

            project_to_delete = PROJECT_INFO.query.get(project_id['project_id'])
            if not project_to_delete:
                return jsonify({"project": "error-notfound"})
            else:
                db.session.delete(project_to_delete)
                db.session.commit()

                get_db_return = PROJECT_INFO.query.filter_by(id=project_id['project_id']).first()
                if not get_db_return:
                    return jsonify({"project": "deleted"})
                else:
                    get_db_return = get_db_return.to_dict()
                    return jsonify(get_db_return)




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




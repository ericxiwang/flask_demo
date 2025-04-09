from flask import request,jsonify
from app.api import flask_api
from .algorithms import *
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import json
@flask_api.route('/',methods=['POST'])
@jwt_required()
def index():
    return "api---1"

@flask_api.route('/api/')
@jwt_required()
def categories():
    return "api-2"


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

@flask_api.route('/list_reverse_slice', methods=['POST','GET'])
@jwt_required()
def list_reverse_slice_api():
    try:
        data = json.loads(request.data)
        user_list = list(data['user_list'])
        new_list = list_reverse_slice(user_list)
        result = {'result':new_list}
        return json.dumps(result)

    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)


@flask_api.route('/list_reverse_loop', methods=['POST','GET'])
@jwt_required()
def list_reverse_loop_api():
    try:
        data = json.loads(request.data)
        user_list = list(data['user_list'])
        new_list = list_reverse_loop(user_list)
        result = {'result':new_list}
        return json.dumps(result)

    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)

@flask_api.route('/list_comprehension', methods=['POST'])
@jwt_required()
def list_comprehension_api():
    try:
        data = json.loads(request.data)
        user_limit = data['user_limit']
        print(user_limit)
        new_list = list_comprehension(user_limit)
        result = {'result': new_list}
        return json.dumps(result)
    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)
@flask_api.route('/fib_loop', methods=['POST'])
@jwt_required()
def fib_loop_api():

    try:
        data = json.loads(request.data)
        user_limit = data['user_limit']
        print(user_limit)
        new_list = fib_loop(user_limit)
        result = {'result': new_list}
        return json.dumps(result)
    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)


@flask_api.route('/fib_recursion_1', methods=['POST'])
@jwt_required()
def fib_recursion_1_api():

    try:
        data = json.loads(request.data)
        user_limit = data['user_limit']
        print(user_limit)
        new_list = fib_loop(user_limit)
        result = {'result': new_list}
        return json.dumps(result)
    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)

@flask_api.route('/fib_recursion_2', methods=['POST'])
@jwt_required()
def fib_recursion_2_api():

    try:
        data = json.loads(request.data)
        user_limit = data['user_limit']
        print(user_limit)
        new_list = fib_recursion_2(user_limit)
        result = {'result': new_list}
        return json.dumps(result)
    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)
@flask_api.route('/build_in_sort', methods=['POST'])
@jwt_required()
def build_in_sort_api():

     try:
         data = json.loads(request.data)
         input_list = data['user_list']
         print(input_list)
         new_list = build_in_sort(input_list)
         result = {'result': new_list}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)

@flask_api.route('/selection_sort', methods=['POST'])
@jwt_required()
def selection_sort_api():

     try:
         data = json.loads(request.data)
         input_list = data['user_list']
         print(input_list)
         new_list = selection_sort(input_list)
         result = {'result': new_list}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/bubble_sort', methods=['POST'])
@jwt_required()
def bubble_sort_api():


     try:
         data = json.loads(request.data)
         input_list = data['user_list']
         new_list = bubble_sort(input_list)
         result = {'result': new_list}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)
@flask_api.route('/quick_sort', methods=['POST'])
@jwt_required()
def quick_sort_api():

     try:
         data = json.loads(request.data)
         input_list = data['user_list']
         new_list = quick_sort(input_list)
         result = {'result': new_list}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)
@flask_api.route('/user_profile', methods=['POST'])
@jwt_required()
def user_profile():

     try:
         user_name      =   "admin_test@test.com"
         user_address   =   "1110-1111 eastwood street"
         user_group     =   "admin"

         result = json.dumps({'user_name': user_name, "user_address":  user_address, "user_group": user_group})

         return result
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)






#========================add several new demo apis
@flask_api.route('/smallest_factor/<input_number>', methods=['GET'])
@jwt_required()
def smallest_factor_api(input_number):
    try:

        prime_number = smallest_factor(int(input_number))
        result = {'smallest_factor':prime_number}
        return json.dumps(result)

    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)



@flask_api.route('/ip_address_generator', methods=['GET'])
@jwt_required()
def ip_address_generator_api():
    try:

        ipv4 = ip_address_generator()
        result = {'ipv4':ipv4}
        return json.dumps(result)

    except:

        help_info = {"user_name": "<email>", "user_password": "<psw>","user_list": "[]"}
        return json.dumps(help_info)

@flask_api.route('/list_find_duplicates', methods=['POST'])
@jwt_required()
def list_find_duplicates_api():

     try:
         data = json.loads(request.data)
         input_list = data['user_list']
         new_list = find_duplicates(input_list)
         result = {'result': new_list}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/list_topKFrequent', methods=['POST'])
@jwt_required()
def list_topKFrequent_api():

     try:
         data = json.loads(request.data)
         words = data['input_words']
         k = data["input_k"]
         new_list = topKFrequent(words,k)
         result = {'result': new_list}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/validate_ipv4_general', methods=['POST'])
@jwt_required()
def validate_ipv4_general_api():

     try:
         data = json.loads(request.data)
         ipv4 = data['ipv4']

         result = {'result': validate_ipv4_general(ipv4)}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/validate_ipv4_regex', methods=['POST'])
@jwt_required()
def validate_ipv4_regex_api():

     try:
         data = json.loads(request.data)
         ipv4 = data['ipv4']

         result = {'result': validate_ipv4_regex(ipv4)}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/validate_email_regex', methods=['POST'])
@jwt_required()
def validate_email_regex_api():

     try:
         data = json.loads(request.data)
         email = data['email']

         result = {'result': validate_email_regex(email)}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/valid_parentheses_nostack', methods=['POST'])
@jwt_required()
def valid_parentheses_nostack_api():

     try:
         data = json.loads(request.data)
         parentheses_string = data['parentheses_string']

         result = {'result': valid_parentheses_nostack(parentheses_string)}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/valid_parentheses_stack', methods=['POST'])
@jwt_required()
def valid_parentheses_stack_api():

     try:
         data = json.loads(request.data)
         parentheses_string = data['parentheses_string']

         result = {'result': valid_parentheses_stack(parentheses_string)}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)


@flask_api.route('/search_insert', methods=['POST'])
@jwt_required()
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
def search_insert_api():

     try:
         data = json.loads(request.data)
         nums = data['nums']
         target = data['target']

         result = {'result': search_insert(nums, int(target))}
         return json.dumps(result)
     except:

         help_info = {"user_name": "<email>", "user_password": "<psw>", "user_list": "[]"}
         return json.dumps(help_info)
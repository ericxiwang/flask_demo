import pytest, requests, json




@pytest.mark.parametrize("test_case_name", ["/api/v1/project_info"])
def test_api_project_info(test_case_name,api_authentication, base_url):
    api_url = base_url + test_case_name
    #test_list = test_data_template[test_case_name]['user_list'][::-1]

    #payload = json.dumps(api_json_temp[test_case_name])

    response = requests.request("GET", api_url, headers=api_authentication,verify=False)
    get_json = response.json()

    #response = requests.get(api_url)

    # Verify status code
    assert response.status_code == 200
    for each_line in get_json:
        print(each_line)
    #assert get_json['result'] == test_list
@pytest.mark.parametrize("test_case_name", ["/api/v1/a_workflow_badge"])
@pytest.mark.parametrize(('json_key','json_value'), [("DoneTickets",3),
                                                 ("InProgressTickets",6),
                                                 ("NewTickets",15),
                                                 ("ReviewTickets",2)])
def test_api_a_workflow_badge(test_case_name,api_authentication, base_url,json_key,json_value):
    api_url = base_url + test_case_name
    response = requests.request("POST", api_url, headers=api_authentication, verify=False)
    get_json = response.json()
    #verify each quantity of tickets
    assert get_json[json_key] == json_value


@pytest.mark.user_management
@pytest.mark.parametrize("test_case_name", ["/api/v1/all_user"])
def test_api_all_user(test_case_name,api_authentication,base_url,local_json_file):

    api_url = base_url + test_case_name
    response = requests.request("GET", api_url, headers=api_authentication, verify=False)
    # compare two jsons between API returns and local file json string
    #assert response.json() == local_json_file[test_case_name]


@pytest.mark.user_management
@pytest.fixture(scope="session")
def test_api_new_user(api_authentication,base_url,local_json_file):
    test_case_name = "/api/v1/user_ops/new"
    new_user = json.dumps(local_json_file[test_case_name])
    api_url = base_url + test_case_name
    response = requests.request("POST", api_url, headers=api_authentication, data=new_user, verify=False)
    get_user_return = response.json()

    assert get_user_return['user_name'] == json.loads(new_user)["user_name"]
    return get_user_return['id']

@pytest.mark.user_management
@pytest.mark.parametrize("test_case_name", ["/api/v1/user_ops/update"])
def test_api_update_user(test_case_name,api_authentication, base_url, test_api_new_user, local_json_file):
    api_url = base_url + test_case_name
    update_id = test_api_new_user
    update_user = local_json_file[test_case_name]
    update_user['id'] = update_id
    print("update user info===",update_user)
    response = requests.request("POST", api_url, headers=api_authentication, data=json.dumps(update_user), verify=False)
    input_data = update_user["email"] + str(update_user["group_id"]) + update_user["user_name"]
    return_date = response.json()["email"] + str(response.json()["group_id"]) + response.json()["user_name"]

    assert input_data == return_date

@pytest.mark.user_management
@pytest.mark.parametrize("test_case_name", ["/api/v1/user_ops/delete"])
def test_api_delete_user(test_case_name,api_authentication,base_url,test_api_new_user):
    api_url = base_url + test_case_name
    delete_id = test_api_new_user
    response = requests.request("POST", api_url, headers=api_authentication, data=json.dumps({"id":delete_id}), verify=False)
    assert response.json()["user"] == "deleted"






import pytest, requests, json
from pytest import assume
with open('dummy_data.json', 'r') as file:
    test_data_template = json.load(file)


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
    assert 1==1
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


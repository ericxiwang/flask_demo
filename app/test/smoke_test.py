import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect

import pytest, re


URL = "http://localhost:3000"
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)

#browser = playwright.chromium.connect("ws://playwright-service:3000")

context = browser.new_context(viewport={'width': 1024, 'height': 768})
page = context.new_page()
page.goto(URL)

page.get_by_placeholder("Enter username").click()
page.get_by_placeholder("Enter username").fill("admin@admin.com")
page.get_by_placeholder("Enter username").press("Tab")
page.get_by_placeholder("Enter password").fill("1234")
page.get_by_role("button", name="Login").click()


@pytest.mark.a_dashboard
@pytest.mark.parametrize("ticket_status,ticket_quantity",[("new",8),("inprogress",5),("review",5),("done",5)])
def test_a_dashboard_main_page(ticket_status,ticket_quantity):

    page.get_by_role("link", name="Agile Dashboard").click()
    page.wait_for_timeout(1000)
    get_all_tickets = page.locator(f"[class*='custom-card-{ticket_status}']").count()

    assert (get_all_tickets == ticket_quantity)
@pytest.mark.a_dashboard
def test_a_dashboard_new_ticket():

    page.get_by_role("button", name="+ CREATE NEW TICKEY +").click()
    page.locator("input[name=\"ticket_title\"]").click()
    page.locator("input[name=\"ticket_title\"]").fill("gui-new-ticket")
    page.locator("input[name=\"ticket_title\"]").press("Tab")
    page.locator("textarea[name=\"ticket_desc\"]").fill("gui-new-ticket-desc")
    page.locator("form div").filter(has_text="User List-- Choose a User --").get_by_role("combobox").select_option("qa_engineer@test.com")
    page.get_by_role("button", name="Add Ticket").click()

@pytest.mark.a_dashboard
def test_a_dashboard_edit_ticket():
    page.locator("//div[text()='gui-new-ticket']/following-sibling::button[1]").click()

    page.locator("input[name=\"ticket_title\"]").click()
    page.locator("input[name=\"ticket_title\"]").fill("edit-title")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save Changes").click()
    page.wait_for_timeout(1000)
    #page.locator("//div[text()='edit-title']/following-sibling::button[1]").click()
@pytest.mark.user_management
def test_user_management_new():
    page.get_by_role("link", name="User Management").click()
    page.get_by_role("button", name="➕ Add User").click()
    page.locator("input[name=\"user_name\"]").click()
    page.locator("input[name=\"user_name\"]").fill("new-user")
    page.locator("input[name=\"user_name\"]").press("Tab")
    page.locator("input[name=\"email\"]").fill("new-user@email.com")
    page.locator("input[name=\"user_password\"]").click()
    page.locator("input[name=\"user_password\"]").fill("1234")
    page.get_by_role("button", name="Add", exact=True).click()

@pytest.mark.user_management
def test_user_management_edit():

    new_user_line = page.locator("//td[text()='new-user@email.com']/following-sibling::td[2]")
    new_user_line.locator("//button[text()='Edit']").click()

    #print("======",get_new_user)
   #
    page.locator("input[name=\"user_name\"]").click()
    page.locator("input[name=\"user_name\"]").fill("new-user-edit")
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("2")
    page.get_by_role("button", name="Save Changes").click()


@pytest.mark.user_management
@pytest.mark.parametrize("user_name,user_email",[("QA001","qa_engineer@test.com"),("new-user-edit","new-user@email.com")])
def test_check_all_users(user_name,user_email):

    get_user_name = page.locator("td", has_text=user_name)
    get_user_email = page.locator("td",has_text=user_email)
    assert get_user_name and get_user_email

@pytest.mark.user_management
@pytest.mark.parametrize("user_name,user_email",[("new-user-edit","new-user@email.com")])
def test_user_management_delete(user_name,user_email):
    delete_user_line = page.locator(f"//td[text()=\'{user_email}\']/following-sibling::td[2]")

    print("+++++++++++++++++++",delete_user_line)
    page.wait_for_timeout(3000)
    delete_user_line.locator("//button[text()='Delete']").click()
    page.wait_for_timeout(3000)

    page.pause()





@pytest.mark.playwright
def test_playwright_GetByRole():
    page.get_by_role("link", name="Agile Task Statistic").click()

    get_headings = page.get_by_role("heading", level=4)
    print(get_headings.inner_text())
    #print("++++++++++++++",get_headings.inner_html())
    assert (get_headings.inner_text() == "Get_By_Role")


@pytest.mark.playwright
def test_playwright_GetByLabel():
    page.get_by_role("link", name="Agile Task Statistic").click()
    get_label_info = page.get_by_label("test_get_by_label")
    assert (get_label_info.input_value() == "col-1")
@pytest.mark.playwright
def test_playwright_GetByPlaceholder():
    page.get_by_role("link", name="Agile Task Statistic").click()
    page.get_by_placeholder("input email").fill("admin@admin.com")

    assert (page.get_by_placeholder("input email").get_attribute("id") == "input4test")

@pytest.mark.playwright
def test_playwright_GetByText():
    page.get_by_role("link", name="Agile Task Statistic").click()
    assert page.get_by_text("text lane").count() == 3

@pytest.mark.playwright
def test_playwright_GetByTitle_1():
    page.get_by_role("link", name="Agile Task Statistic").click()
    assert page.get_by_title("get_by_title").count() == 3
@pytest.mark.playwright
def test_playwright_GetByTitle_2():
    page.get_by_role("link", name="Agile Task Statistic").click()

    assert page.get_by_title("get_by_title").filter(has_not_text="option-1").count() == 2
@pytest.mark.playwright
def test_playwright_GetByTestId():
    page.get_by_role("link", name="Agile Task Statistic").click()
    page.wait_for_selector("[data-testid='test_table']")

    table = page.get_by_test_id("test_table")
    rows = table.locator("tr")

    row_count = rows.count()
    print("Row count:", row_count)

    get_the_last_row = rows.nth(row_count-1)
    get_the_last_cell = get_the_last_row.locator("td").nth(2)
    print(f'get the last cell from table: {get_the_last_cell.inner_text()}')
    assert (get_the_last_cell.inner_text() == "Data 9")
@pytest.mark.playwright
def test_playwright_sibling():
    page.get_by_role("link", name="Agile Task Statistic").click()
    page.wait_for_selector("div[class='sibling_test_div']")
    get_elements = page.locator("div[class='sibling_test_div']")

    get_button = get_elements.locator("//following-sibling::button")
    print(get_button.get_attribute("name"))

    get_p_elements = get_elements.locator("//following-sibling::p[2]")
    print(get_p_elements.get_attribute("name"))
    assert (get_p_elements.get_attribute("name") == "name_element-6" and get_button.get_attribute("name") == "name_element-4")

@pytest.mark.playwright
def test_playwright_parents():
    page.get_by_role("link", name="Agile Task Statistic").click()
    page.wait_for_selector("css=ul")
    get_list_item = page.get_by_role("listitem").filter(has_text="Coffee")
    get_parent_list = page.locator("ul").filter(has=get_list_item)
    print(f"return name of this element : {get_parent_list.get_attribute('name')}")
    assert (get_parent_list.get_attribute('name') == "parent_sub_list")

@pytest.mark.playwright
@pytest.mark.parametrize("input_name",[1,2,3,4])
def test_playwright_elements_nth(input_name):
    page.get_by_role("link", name="Agile Task Statistic").click()
   # get_parent_div = page.locator('[name="nth_test_div"]').locator("/input[1]").fill("test")
    get_single_input = page.locator(f"div[name='nth_test_div'] input:nth-child({input_name})")
    #get_input_list = get_parent_div.locator("//following-sibling::input")
    #get_inputs = get_parent_div.locator('css=input')
    #print(get_inputs.count())
    print("_____________",get_single_input.get_attribute('name'))
    assert (get_single_input.get_attribute('name') == ("input-"+str(input_name)))

@pytest.mark.playwright
@pytest.mark.parametrize("input_color,return_attribute",[("rgb(255, 0, 0)","red-div"),("rgb(0, 255, 0)","green-div")])
def test_playwright_elements_css_validation(input_color,return_attribute):
    page.get_by_role("link", name="Agile Task Statistic").click()
    page.wait_for_selector("css=div")
    divs = page.locator("div")
    count = divs.count()

    result = False
    for i in range(count):
        bg = divs.nth(i).evaluate("el => getComputedStyle(el).backgroundColor")
        div_name = divs.nth(i).get_attribute('name')

        if bg == input_color and div_name == return_attribute:
            print(f"found{input_color} in {div_name}")
            result = True
    assert result


def test_done():
    # ---------------------
    context.close()
    browser.close()



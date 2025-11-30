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

def test_a_dashboard_new_ticket():
    page.get_by_role("button", name="+ CREATE NEW TICKEY +").click()
    page.locator("input[name=\"ticket_title\"]").click()
    page.locator("input[name=\"ticket_title\"]").fill("gui-new-ticket")
    page.locator("input[name=\"ticket_title\"]").press("Tab")
    page.locator("textarea[name=\"ticket_desc\"]").fill("gui-new-ticket-desc")
    page.locator("form div").filter(has_text="User List-- Choose a User --").get_by_role("combobox").select_option("qa_engineer@test.com")
    page.get_by_role("button", name="Add Ticket").click()

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
def test_done():
    # ---------------------
    context.close()
    browser.close()



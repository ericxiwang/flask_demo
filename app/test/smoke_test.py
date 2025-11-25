import re
from playwright.sync_api import Playwright, sync_playwright, expect

import pytest, re


URL = "http://localhost:3000"
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)

#browser = playwright.chromium.connect("ws://playwright-service:3000")
context = browser.new_context()
page = context.new_page()
page.goto(URL)
def test_login():

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

    #page.locator("input[name=\"ticket_title\"]").click()
    page.locator("input[name=\"ticket_title\"]").fill("edit-title")
    page.get_by_role("button", name="Save Changes").click()

    page.locator("//div[text()='dit-title']/following-sibling::button[1]").click()


    # ---------------------
    context.close()
    browser.close()



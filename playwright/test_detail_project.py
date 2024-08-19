import re
from playwright.sync_api import Page, expect
import pytest
import math


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("http://localhost:8001/")
    page.get_by_role("link", name="Login/Sign Up").click()
    page.get_by_placeholder("Enter your username...").click()
    page.get_by_placeholder("Enter your username...").fill("testuser")
    page.get_by_placeholder("Enter your username...").press("Tab")
    page.get_by_placeholder("••••••••").fill("testpassword123")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="x").click()
    page.get_by_role("link", name="Projects").click()
    page.get_by_role("link", name="project thumbnail").first.click()
    yield
    
@pytest.fixture(scope="module", autouse=True)
def before_login(page: Page):
    page.goto("http://localhost:8001/projects/")
    page.get_by_role("link", name="DEnnis Portifolio").click()
    expect(page.get_by_test_id("comment-form")).not_to_be_visible()

def test_initial_number_comments(page: Page):
    expect(page.get_by_test_id("comment")).to_have_count(1)


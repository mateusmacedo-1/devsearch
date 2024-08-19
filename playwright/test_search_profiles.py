import re
from playwright.sync_api import Page, expect
import pytest
import math


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    page.goto("http://localhost:8001/")
    page.get_by_role("link", name="Developers").click()
    yield
    
    print("after the test runs")

    
def test_has_title(page: Page):
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("DevSearch"))

def test_has_search_button(page: Page):
    expect(page.get_by_role("button", name="Search")).to_be_visible()

def test_has_heading_equivalent_to_page(page: Page):
    expect(page.get_by_role("main")).to_contain_text("CONNECT WITH DEVELOPERS FROM AROUND THE WORLD")

def test_search_results(page: Page):
    page.get_by_test_id('search-input').fill("dasefhmji615165")
    page.get_by_test_id('search-button').click()
    p = page.get_by_test_id('profiles')
    expect(p).not_to_be_visible()


def search_by_tag(page: Page, tag: str, number_of_items, page_length):
    page.get_by_test_id('search-input').fill(tag)
    page.get_by_test_id('search-button').click()
    expect(page.get_by_test_id("profile")).to_have_count(min(number_of_items, page_length))
    for i in range(min(number_of_items, page_length)):
        expect(page.get_by_test_id("tags").nth(i)).to_contain_text(tag, ignore_case=True)
    if number_of_items <= 3:
        expect(page.get_by_test_id("pagination")).not_to_be_visible()
    else:
        expect(page.get_by_test_id("pagination")).to_be_visible()
        expect(page.get_by_test_id("page-number")).to_have_count(math.ceil(number_of_items / page_length))

def search_by_tag(page: Page, tag: str, number_of_items, page_length):
    page.get_by_test_id('search-input').fill(tag)
    page.get_by_test_id('search-button').click()
    expect(page.get_by_test_id("profile")).to_have_count(min(number_of_items, page_length))
    for i in range(min(number_of_items, page_length)):
        expect(page.get_by_test_id("tags").nth(i)).to_contain_text(tag, ignore_case=True)
    if number_of_items <= 3:
        expect(page.get_by_test_id("pagination")).not_to_be_visible()
    else:
        expect(page.get_by_test_id("pagination")).to_be_visible()
        expect(page.get_by_test_id("page-number")).to_have_count(math.ceil(number_of_items / page_length))

def search_by_title(page: Page, search_string: str, number_of_items, page_length):
    page.get_by_test_id('search-input').fill(search_string)
    page.get_by_test_id('search-button').click()
    expect(page.get_by_test_id("profile")).to_have_count(min(number_of_items, page_length))
    for i in range(min(number_of_items, page_length)):
        expect(page.get_by_test_id("profile").nth(i)).to_contain_text(search_string, ignore_case=True)
    if number_of_items <= 3:
        expect(page.get_by_test_id("pagination")).not_to_be_visible()
    else:
        expect(page.get_by_test_id("pagination")).to_be_visible()
        expect(page.get_by_test_id("page-number")).to_have_count(math.ceil(number_of_items / page_length))

def test_search_by_tag(page: Page):
    page_length = 3
    tags = [
        {
            'name': 'python',
            'number_of_items': 2,
            
        },
        {
            'name': 'django',
            'number_of_items': 1,
            
        },
        {
            'name': 'figma',
            'number_of_items': 1,
        },
    ]
    for tag in tags:
        search_by_tag(page, tag['name'], tag['number_of_items'], page_length)

def test_search_by_username(page: Page):
    page_length = 3
    search_strings = [
        {
            'name': 'mateus',
            'number_of_items': 1,
            
        },
        {
            'name': 'júlio',
            'number_of_items': 1,
            
        },
        {
            'name': 'yoshiga',
            'number_of_items': 1,
        },
    ]
    for search_string in search_strings:
        search_by_title(page, search_string['name'], search_string['number_of_items'], page_length)
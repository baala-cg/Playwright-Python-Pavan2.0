
"""If a dependency fails

If test_login fails:

test_login → Failed
test_add_product → Skipped
test_checkout → Skipped
"""

import pytest

@pytest.mark.dependency(name="login")
def test_login():
    print("Login successful")
    assert True

@pytest.mark.dependency(depends=["login"])
def test_add_product():
    print("Product added")
    assert True

@pytest.mark.dependency(depends=["test_add_product"])
def test_checkout():
    print("Checkout completed")
    assert True


import pytest

@pytest.mark.dependency(name="login")
def test_login():
    assert True

@pytest.mark.dependency(name="add_product", depends=["login"])
def test_add_product():
    assert True

@pytest.mark.dependency(depends=["add_product"])
def test_checkout():
    assert True


"""
However, this is generally not recommended

In Playwright automation, tests should ideally be independent. Chaining tests together creates several problems:

A single failed test causes many others to be skipped.
Tests become difficult to run individually.
Parallel execution is limited.
Debugging becomes harder.

A better approach is to use fixtures for shared setup:
"""

import pytest

@pytest.fixture
def logged_in_page(page):
    page.goto("https://example.com")
    # Login steps
    return page

def test_create_order(logged_in_page):
    page = logged_in_page
    # Test code

def test_delete_order(logged_in_page):
    page = logged_in_page
    # Test code
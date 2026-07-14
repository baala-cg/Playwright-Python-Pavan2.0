from playwright.sync_api import sync_playwright, expect, Playwright
import pytest


def test_tabs(playwright: Playwright):
    # Launch browser and create context/page
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parentpage = context.new_page()

    # Navigate to the target page
    parentpage.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


   #Register event for popup - Get all popups when they open
    parentpage.on("page", lambda page: page.wait_for_load_state())

    parentpage.locator("a:has-text('OrangeHRM, Inc')").click()

    parentpage.wait_for_timeout(5000)

    # Get all tab pages
    all_pages = context.pages
    print("Number of pages/windows:", len(all_pages))

    # Print all page URLs
    for tab in all_pages:
        print("Window  URL===> ", tab.url)

    # switch between pages and get titles ( using context)
    print("Title of the Parent Page:",all_pages[0].title())
    print("Title of the Child Page:", all_pages[1].title())




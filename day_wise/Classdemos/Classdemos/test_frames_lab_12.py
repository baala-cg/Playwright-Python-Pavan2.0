import pytest
from playwright.sync_api import sync_playwright, expect


def test_frame1_fill_and_assert_input_field(page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame1 = page.frame_locator('frame[src="frame_1.html"]')
    frame1.locator('input[name="mytext1"]').fill("Welcome")
    expect(frame1.locator('input[name="mytext1"]')).to_have_value("Welcome")


def test_frame2_fill_and_assert_input_field(page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame2 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_2.html")
    frame2.locator('input[name="mytext2"]').fill("Suneel")
    expect(frame2.locator('input[name="mytext2"]')).to_have_value("Suneel")


def test_frame3_handle_nested_frame_and_form(page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")

    frame3.locator('[name="mytext3"]').fill("You are in Frame 3 - Teal")
    expect(frame3.locator('[name="mytext3"]')).to_have_value("You are in Frame 3 - Teal")

    child_frames = frame3.child_frames
    child = child_frames[0]

    child.get_by_role("radio", name="Hi, I am the UI.Vision IDE").click()
    child.get_by_role("checkbox", name="Form Autofilling").click()

    child.get_by_role("option", name="Choose").click()
    page.wait_for_timeout(2000)
    child.get_by_role("option", name="Yes").click()
    page.wait_for_timeout(2000)

    child.get_by_role("button", name="Next").click()

    short_text = child.get_by_role("textbox", name="Enter a short text")
    short_text.fill("We are here")
    expect(short_text).to_have_value("We are here")

    long_text = child.get_by_role("textbox", name="Enter a long answer")
    long_text.fill("We are able to access all element in child frame")
    expect(long_text).to_have_value("We are able to access all element in child frame")

    child.get_by_role("button", name="Submit").click()
    confirmation_text = child.locator(".vHW8K").inner_text()
    print(confirmation_text)


def test_frame5_fill_input_and_verify_logo(page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame5 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_5.html")

    frame5.locator('input[name="mytext5"]').fill("playwright")
    expect(frame5.locator('input[name="mytext5"]')).to_have_value("playwright")

    frame5.locator('a[href="https://a9t9.com"]').click()
    page.wait_for_timeout(5000)

    logo = frame5.locator("img.responsive-img").first
    expect(logo).to_be_visible()

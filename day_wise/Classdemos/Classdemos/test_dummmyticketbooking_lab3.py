import pytest
from playwright.sync_api import sync_playwright, Page, expect


def select_date_of_birth(page, birth_year, birth_month, birth_date):
    # Select Year
    page.locator('select[data-handler="selectYear"]').select_option(birth_year)

    # Select Month
    page.locator('select.ui-datepicker-month').select_option(birth_month)

    # Select Date
    date_cells = page.locator('table.ui-datepicker-calendar td a').all()
    for cell in date_cells:
        if cell.text_content() == birth_date:
            cell.click()
            break


def select_date(page, required_year, required_month, required_date):
    # Select Year
    page.locator('select[data-handler="selectYear"]').select_option(required_year)

    # Select Month
    page.locator('select[aria-label="Select month"]').select_option(required_month)

    # Select Date
    date_cells = page.locator('table.ui-datepicker-calendar td a').all()
    for cell in date_cells:
        if cell.text_content() == required_date:
            cell.click()
            break


def test_dummy_ticket_booking(page: Page):
    # Launch the URL
    page.goto('https://www.dummyticket.com/dummy-ticket-for-visa-application/')

    # Assert page title
    expect(page).to_have_title("Dummy ticket for applying visa - Verifiable flight reservation for embassy")

    # Choose the correct option: Dummy ticket for Visa Application radio option
    page.locator('#product_549').check()
    expect(page.locator('#product_549')).to_be_checked()

    # Passenger details
    page.locator('[name="travname"]').fill('Akash')
    page.locator('#travlastname').fill('Ratore')

    # Select Date Of Birth
    birth_year = "2001"
    birth_month = "Mar"
    birth_date = "2"
    page.locator('#dob').click()
    select_date_of_birth(page, birth_year, birth_month, birth_date)

    # Verify date was selected
    dob_value = page.locator('#dob').input_value()
    print("DOB Value====>", dob_value)
    expect(page.locator('#dob')).to_have_value('02/03/2001')

    # Select sex
    page.locator('#sex_1').check()
    expect(page.locator('#sex_1')).to_be_checked()

    # Travel Details
    page.locator('#traveltype_1').check()
    expect(page.locator('#traveltype_1')).to_be_checked()
    page.locator('[name="fromcity"]').fill('Toronto')
    page.locator('[name="tocity"]').fill('Mumbai')

    # Select departure date
    required_year = "2025"
    required_month = "Nov"
    required_date = "25"
    page.locator('#departon').click()
    select_date(page, required_year, required_month, required_date)

    # Verify departure date was selected
    depart_value = page.locator('#departon').input_value()
    print("Departure Value====>", depart_value)
    expect(page.locator('#departon')).to_have_value('25/11/2025')


    # Additional information
    page.locator('#notes').fill('Need visa as soon as possible')
    expect(page.locator('#notes')).to_have_value('Need visa as soon as possible')

    # Delivery options
    page.locator('#select2-reasondummy-container').click()
    page.locator('.select2-results li:first-child').click()

    # Select appointment date
    appt_year = "2025"
    appt_month = "Dec"
    appt_date = "10"
    page.locator('#appoinmentdate').click()
    select_date(page, appt_year, appt_month, appt_date)

    # Verify Appointment / Submission date  was selected
    appt_value = page.locator('#appoinmentdate').input_value()
    print("Appointment / Submission Value====>", appt_value)
    expect(page.locator('#appoinmentdate')).to_have_value('10/12/2025')

    # Notification
    page.locator('#deliverymethod_1').check()
    expect(page.locator('#deliverymethod_1')).to_be_checked()

    # Billing Details
    page.locator('#billname').fill('Akash Rathore')
    page.locator('[name="billing_phone"]').fill('+12345678956')
    page.locator('#billing_email').fill('abc.123@gmail.com')

    # Select country
    page.locator('#select2-billing_country-container').click()
    page.locator('.select2-results li:has-text("Canada")').click()

    page.locator('#billing_address_1').fill('123 Scott Street')
    page.locator('[name="billing_city"]').fill('Niagara Falls')

    # Select state
    page.locator('#select2-billing_state-container').click()
    page.locator('.select2-results li:has-text("Ontario")').click()

    page.locator('#billing_postcode').fill('L2C 6M1')

    # Verify billing details
    expect(page.locator('#billname')).to_have_value('Akash Rathore')
    expect(page.locator('[name="billing_phone"]')).to_have_value('+12345678956')
    expect(page.locator('#billing_email')).to_have_value('abc.123@gmail.com')
    expect(page.locator('#select2-billing_country-container')).to_have_text('Canada')
    expect(page.locator('#billing_address_1')).to_have_value('123 Scott Street')
    expect(page.locator('[name="billing_city"]')).to_have_value('Niagara Falls')
    expect(page.locator('#select2-billing_state-container')).to_have_text('Ontario')
    expect(page.locator('#billing_postcode')).to_have_value('L2C 6M1')

    # Verify Product details table
    product_name = page.locator('.product-details')
    print("Product Name=====>:", product_name.inner_text())
    expect(product_name).to_have_text("Dummy return ticket")

    product_price = page.locator('.shop_table.woocommerce-checkout-review-order-table tfoot tr:nth-child(2) td')
    print("Product Price=====>:",product_price.inner_text())
    expect(product_price).to_have_text("₹990")

    # Place order
    page.locator('#place_order').click()

from playwright.sync_api import Playwright, sync_playwright, expect, Page

def test_single_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # Upload single file
    page.locator("#filesToUpload").set_input_files("uploads/testfile1.pdf")

    # Validate file uploaded
    expect(page.locator("#fileList li:nth-child(1)")).to_have_text("testfile1.pdf")
    page.wait_for_timeout(5000)



def test_multiple_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # Upload multiple files
    files = ["uploads/testfile1.pdf", "uploads/testfile2.pdf"]
    page.locator("#filesToUpload").set_input_files(files)

    # Validate file names
    expect(page.locator("#fileList li:nth-child(1)")).to_have_text("testfile1.pdf")
    expect(page.locator("#fileList li:nth-child(2)")).to_have_text("testfile2.pdf")

    # Remove all selected files (clear input)
    page.locator("#filesToUpload").set_input_files([])

    # Validate cleared state
    expect(page.locator("#fileList li:nth-child(1)")).to_have_text("No Files Selected")

    page.wait_for_timeout(5000)

from playwright.sync_api import sync_playwright

def run_test():
    print("Starting Playwright test...")

    with sync_playwright() as p:
        # Launch Chromium in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Visit a test page
        page.goto("https://example.com")

        # Print result
        print("Page title:", page.title())

        browser.close()

if __name__ == "__main__":
    run_test()

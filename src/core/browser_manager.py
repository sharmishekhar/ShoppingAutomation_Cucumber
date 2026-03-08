from playwright.sync_api import sync_playwright


class BrowserManager:

    def start_browser(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=True)
        return playwright, browser
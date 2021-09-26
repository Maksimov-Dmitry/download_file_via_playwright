from playwright.sync_api import sync_playwright, Page, Download
from datetime import date


def download(page: Page) -> Download:
    
        # Go to https://etf.dws.com/en-us/DBJP-msci-japan-hedged-equity-etf/
        page.goto("https://etf.dws.com/en-us/DBJP-msci-japan-hedged-equity-etf/")
    
        # Click text=Accept and proceed
        page.click("text=Accept and proceed")
    
        # Click .audience-selection__item-overlay
        page.click(".audience-selection__item-overlay")
    
        # Click text=Accept
        # with page.expect_navigation(url="https://etf.dws.com/en-us/DBJP-msci-japan-hedged-equity-etf/"):
        with page.expect_navigation():
            page.click("text=Accept")
    
        # Click text=Download Fund Holdings
        with page.expect_download() as download_info:
            with page.expect_popup():
                page.click("text=Download Fund Holdings")
        return download_info.value
        
        
if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        # Open new page
        page = context.new_page()
        file = download(page)
        file.save_as(f'./fund_holdings_{date.today()}.xlsx')
        file.delete()
    
        # ---------------------
        context.close()
        browser.close()
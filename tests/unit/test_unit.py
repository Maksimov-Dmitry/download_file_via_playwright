from src.main import download

def test_selectors(page):
    """
    This test checks for selectors to download
    """
    page.goto("https://etf.dws.com/en-us/DBJP-msci-japan-hedged-equity-etf/")
    
    accept_button_1 = page.wait_for_selector("text=Accept and proceed")
    visible_accept_button_1 = accept_button_1.is_visible()
    assert visible_accept_button_1
    
    page.click("text=Accept and proceed")
    
    role_type = page.wait_for_selector(".audience-selection__item-overlay")
    visible_role_type = role_type.is_visible()
    assert visible_role_type
    
    page.click(".audience-selection__item-overlay")
    
    accept_button_2 = page.wait_for_selector("text=Accept")
    visible_accept_button_2 = accept_button_2.is_visible()
    assert visible_accept_button_2
    
    with page.expect_navigation():
        accept_button_2 = page.wait_for_selector("text=Accept")
        visible_accept_button_2 = accept_button_2.is_visible()
        assert visible_accept_button_2
        
        page.click("text=Accept")
        
    download_button = page.wait_for_selector("text=Download Fund Holdings")
    visible_download_button = download_button.is_visible()
    assert visible_download_button
        
def test_unit_download(mocker):
    """
    This test checks for download functionality in a download function
    """
    page = mocker.MagicMock()
    download(page)
    page.goto.assert_called_with("https://etf.dws.com/en-us/DBJP-msci-japan-hedged-equity-etf/")
    calls = [mocker.call.click("text=Accept and proceed"),
              mocker.call.click(".audience-selection__item-overlay"),
              mocker.call.click("text=Accept"),
              mocker.call.click("text=Download Fund Holdings")]
    page.assert_has_calls(calls, any_order=True)
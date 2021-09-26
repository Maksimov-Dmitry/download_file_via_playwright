def test_accept_button(page):
    page.goto("/")
    
    accept_button = page.wait_for_selector("#consent_prompt_submit")
    visible = accept_button.is_visible()
    
    assert visible
    
# def test_accept_button(page):
#     page.goto("/")
    
#     accept_button = page.wait_for_selector("#consent_prompt_submit")
#     visible = accept_button.is_visible()
    
#     assert visible
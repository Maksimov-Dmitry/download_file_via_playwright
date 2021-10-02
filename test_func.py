from main import download

def test_func_download(page):
    """
    This test checks for download errors
    """
    assert download(page).failure() is None
from main import download

def test_download(page):
    assert download(page).failure() is None
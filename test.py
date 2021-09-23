from main import download
import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False
    }

@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "accept_downloads": True
    }


def test_download(page):
    assert download(page).failure() is None
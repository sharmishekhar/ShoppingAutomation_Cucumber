import pytest
from src.utilities.data_loader import get_login_data

@pytest.mark.parametrize("data", get_login_data())
def test_login(page, data):

    page.fill("#loginFrm_loginname", data["username"])
    page.fill("#loginFrm_password", data["password"])
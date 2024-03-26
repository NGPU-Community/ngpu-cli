# -- coding: utf-8 --
import requests

from cli import CLOUD_HOST


def mock_login_cloud():
    """
    mock login cloud admin
    @:arg:
    """
    url = "{}/user/login".format(CLOUD_HOST)
    data = {
        "username": "admin",
        "password": "111111"
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()["authorization"]
        raise SystemExit('mock login cloud failed: {}'.format(response.json()))
    except Exception as e:
        raise SystemExit(e)

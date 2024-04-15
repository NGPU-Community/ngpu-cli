# -- coding: utf-8 --
import hashlib

import requests

from cli import CLOUD_HOST


def mock_login_cloud():
    """
    mock login cloud admin
    @:arg:
    """
    url = "{}/ngpu/api/v1/user/login".format(CLOUD_HOST)
    data = {
        "email": "admin@admin.com",
        "password": hashlib.md5("111111".encode()).hexdigest()
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()["result"]["token"]
        raise SystemExit('mock login cloud failed: {}'.format(response.json()))
    except Exception as e:
        raise SystemExit(e)

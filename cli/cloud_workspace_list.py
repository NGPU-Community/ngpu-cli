# -- coding: utf-8 --
import json
import logging

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def cloud_workspace_list(args):
    """
    cli: main.py cloud-workspace-list
    @:arg:
    """

    id = args.id

    login = mock_login_cloud()
    headers = {
        'Token': login,
    }

    url = "{}/ngpu/api/v1/cloud/workspace/list".format(CLOUD_HOST)

    data = {
        "id": id
    }

    response = requests.get(url, headers=headers, data=data)
    logging.info(response.text)
    if response.status_code == 200:
        print(json.dumps(response.json()['result'], indent=4))
    else:
        logging.error('cloud workspace list failed: {}'.format(response.text))

import json
import logging

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def cloud_workspace_group_list(args) -> None:
    id = args.id

    login = mock_login_cloud()
    headers = {
        'Token': login,
    }

    url = "{}/ngpu/api/v1/cloud/workspace/group/selector".format(CLOUD_HOST)

    response = requests.get(url, headers=headers)
    logging.info(response.text)
    if response.status_code == 200:
        print(json.dumps(response.json()['result'], indent=4))
    else:
        logging.error('cloud workspace group list failed: {}'.format(response.text))

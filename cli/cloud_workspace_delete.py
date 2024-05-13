import json
import logging

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def cloud_workspace_delete(args):
    # check param
    workspace_id = args.id

    if workspace_id is None:
        raise SystemExit('cloud-workspace-delete failed: --id is null')

    # mock login admin, get token
    login = mock_login_cloud()
    headers = {
        'Token': login,
    }

    url = f"{CLOUD_HOST}/ngpu/api/v1/cloud/workspace/delete/{workspace_id}"

    response = requests.get(url, headers=headers)
    logging.info(response.text)
    if response.status_code == 200:
        print(json.dumps(response.json()['result'], indent=4))
    else:
        logging.error('cloud image list failed: {}'.format(response.text))

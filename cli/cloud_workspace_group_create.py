import logging

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def cloud_workspace_group_create(args) -> None:
    name = args.name

    if name is None or name == '':
        logging.error('cloud-workspace-group-create failed: name is required')
        return

    login = mock_login_cloud()
    headers = {
        'Token': login,
    }

    url = "{}/ngpu/api/v1/cloud/workspace/group/create".format(CLOUD_HOST)

    data = {
        "workspace_group_name": name,
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        logging.info(response.text)
        if response.status_code == 200:
            logging.info(
                'cloud-workspace-group-create result: work group id[{}]'.format(
                    response.json()['result']['workspace_group_id']))
            return

        # not 200
        logging.error('cloud-workspace-group-create failed: {}'.format(response.text))
    except Exception as err:
        raise err

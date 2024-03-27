# -- coding: utf-8 --
import logging

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def cloud_workspace_create(args):
    # check param
    workspace_name = args.name
    image_id = args.image_id
    product_id = args.product_id
    node_num = args.node_num
    unit = args.unit
    duration = args.duration

    is_group = False
    workspace_group_id = ''
    if node_num > 1:
        is_group = True
        workspace_group_id = 'group_id'

    area = '*'
    public_network = 1

    # mock login admin, get token
    login = mock_login_cloud()
    headers = {
        'Content-Type': 'application/json',
        'Token': login,
    }

    url = "{}/ngpu/api/v1/cloud/workspace/create".format(CLOUD_HOST)

    data = {
        "workspace_name": workspace_name,
        "area": area,
        "duration": duration,
        "duration_unit": unit,
        "public_net": public_network,
        "num": node_num,
        "image_id": image_id,
        "product_id": product_id,
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        logging.info(response.text)
        if response.status_code == 200:
            logging.info('cloud-workspace-create result: work id[{}]'.format(response.json()['result']['workspace_id']))
            return

        # not 200
        logging.error('cloud-workspace-create failed: {}'.format(response.text))
    except Exception as err:
        raise err

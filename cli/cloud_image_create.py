# -- coding: utf-8 --
import logging

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def cloud_image_create(args):
    """
    cli: main.py image-create
    @:arg: --name=<name> image name string
    @:arg: --wget-url=<url> download docker tar file url string, not dockerhub
    @:arg: --note=<note> descirption for docker image
    @:arg: --start=<start> docker run string
    @:arg: --ports=<ports> docker run ports mapping string: ep. "8080:80,8081:81"
    @:arg: --docker-image-id=<id> docker image id string
    """
    # mock login admin, get token
    login = mock_login_cloud()

    image_name = args.name
    image_docker_hub = ''
    note = args.note
    action = 1
    start_cmd = args.start
    stop_cmd = ''
    port_mapping = args.ports
    exception = 1
    docker_image_id = args.docker_image_id
    image_type = 1
    wget_url = args.wget_url

    url = "{}/ngpu/api/v1/cloud/image/create".format(CLOUD_HOST)

    headers = {
        'Content-Type': 'application/json',
        'Token': login,
    }

    data = {
        "image_name": image_name,
        "type": image_type,
        "wget_url": wget_url,
        "note": note,
        "action": action,
        "start_cmd": start_cmd,
        "stop_cmd": stop_cmd,
        "port_mapping": port_mapping,
        "exception": exception,
        "docker_image_id": docker_image_id,
        "file_size": 0,
        "file_path": ""
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        logging.info(response.text)
        if response.status_code == 200:
            logging.info('cloud-image-create result: image id[{}]'.format(response.json()['result']['image_id']))
            return

        # not 200
        logging.error('cloud-image-create failed: {}'.format(response.json()))
    except Exception as err:
        raise err

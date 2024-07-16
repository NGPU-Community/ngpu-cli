import json
import logging
import time
from datetime import datetime

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud


def demo_llm(args):
    # create ai model workspace
    workspace_name = "demo-llm-" + datetime.now().strftime('%Y%m%d%H%M%S')
    image_id = "380608029659235328"
    product_id = "10"
    unit = "week"
    duration = 1
    node_num = 1
    is_group = False
    public_network = 1
    area = '*'
    workspace_group_id = ""

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
        "is_group": is_group,
        "workspace_group_id": workspace_group_id,
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        logging.info(response.text)
        if response.status_code == 200:
            logging.info('cloud-workspace-create result: work id[{}]'.format(response.json()['result']['workspace_id']))
        else:
            logging.error('cloud-workspace-create failed: {}'.format(response.text))
            return
    except Exception as err:
        raise err

    # waiting workspace ready
    workspace_id = response.json()['result']['workspace_id']
    # workspace_id = 370450138809762816
    url = f"{CLOUD_HOST}/ngpu/api/v1/cloud/workspace/list?id={workspace_id}"

    while True:
        print("waiting workspace ready, 60s after retry...")
        response = requests.get(url, headers=headers, data=data)
        logging.info(response.text)
        if response.status_code == 200:

            result = response.json()['result'][0]

            status = result['docker_state']
            id = result['id']
            name = result['workspace_name']
            node_list = result['node_list']

            if status == 4 and len(node_list) > 0 and node_list[0]['rStatus'] == 1:
                break

        time.sleep(60)

    print("workspace ready finish")
    # workspace_id = 380555277914604544

    print("call ai model...")
    while True:
        content = input("\nplease input your question, 'quit' exit:\n")
        if content == 'quit':
            print("exit...")
            break
        # call the model to get the answer

        url = 'https://ainngpu.io/user/schedulingTask?paramUrl=startSync&paramPort=8075'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer ngpu_{workspace_id}',
        }
        body = {
            "btc_address": "bc1pp8vyhh2ma0ntzjwr26xxrn5r0w296yu68wdwle5rrhgtv3a2lgkqtyayus",
            "data": '{"prompt":"%s"}' % content
        }
        answer = ""
        try:
            response = requests.post(url, headers=headers, json=body)
            logging.info(response.text)
            if response.status_code == 200 and response.json()['result_code'] == 200:
                task_id = response.json()['taskId']
            else:
                logging.error('create task failed: {}'.format(response.text))
                return

            # waiting task result
            url = f'https://ainngpu.io/user/queryTask?taskID={task_id}'
            while True:
                # print("waiting ai task ready, 60s after retry...")
                response = requests.get(url)
                # logging.info(response.text)
                if response.status_code == 200 and response.json()['result_code'] == 200 and response.json()[
                    'result_size'] > 0:
                    json_data = json.loads(response.json()['data'])
                    # print(json.dumps(json_data['data'], indent=4))
                    answer = json_data['data']
                    break

                time.sleep(8)
        except Exception as err:
            raise err

        print(f"\nAnswer:\n {answer}\n")

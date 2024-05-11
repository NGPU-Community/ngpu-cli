import io
import json
import logging
import os
import time
from datetime import datetime

import requests

from cli import CLOUD_HOST
from utils.cloud_utils import mock_login_cloud
import base64
from PIL import Image
from io import BytesIO


def demo(args):
    # create workspace

    workspace_name = "demo-" + datetime.now().strftime('%Y%m%d%H%M%S')
    image_id = "352004784519119872"
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

    # TODO check docker start

    print("use workspace to create task")

    # TODO create task
    url = "https://ainngpu.io/user/createImage"
    # bc1pp8vyhh2ma0ntzjwr26xxrn5r0w296yu68wdwle5rrhgtv3a2lgkqtyayus
    btc_addr = 'bc1pp8vyhh2ma0ntzjwr26xxrn5r0w296yu68wdwle5rrhgtv3a2lgkqtyayus'
    headers1 = {
        'BtcAddress': btc_addr,
        'Authorization': str(workspace_id),
        'Content-Type': 'application/json',
    }

    current_project_path = os.getcwd()

    filename = os.path.join(current_project_path, 'demo_file', 'demo_input.jpeg')  # Replace with your image file name
    base64_string = image_to_base64(filename)
    data = {
        "init_images":
            [
                "data:image/jpeg;base64," + base64_string,
            ],
        "resize_mode": 1,
        "denoising_strength": 0.6000000000000001,
        "prompt": ",NSFW, Best quality, masterpiece, ultra high res, RAW photo, (photorealistic:1.4),",
        "steps": 40,
        "cfg_scale": 7.5,
        "width": 720,
        "height": 720,
        "restore_faces": False,
        "negative_prompt": "Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra limb, ugly, poorly drawn hands, missing limb, blurry, floating limbs, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, ((((mutated hands and fingers)))), (((out of frame)))",
        "sampler_index": "Euler a",
        "include_init_images": False,
        "alwayson_scripts":
            {
                "controlnet":
                    {
                        "args":
                            [
                                {
                                    "input_image": "data:image/jpeg;base64," + base64_string,
                                    "mask": "",
                                    "module": "preprocessor: canny",
                                    "model": "control_v11p_sd15_lineart [43d4be0d]",
                                    "weight": 0.2,
                                    "resize_mode": "Scale to Fit (Inner Fit)",
                                    "lowvram": False,
                                    "processor_res": 64,
                                    "threshold_a": 64,
                                    "threshold_b": 64,
                                    "guidance_start": 0,
                                    "guidance_end": 1,
                                    "control_mode": 0,
                                    "pixel_perfect": False
                                }
                            ]
                    }
            }
    }

    response = requests.post(url, headers=headers1, json=data)
    logging.info(response.text)
    if response.status_code == 200 and response.json()['result_code'] == 200:
        task_id = response.json()['taskId']
    else:
        logging.error('create task failed: {}'.format(response.text))
        return

    # waiting task result
    url = 'https://ainngpu.io/user/getImage?taskID={}'.format(task_id)
    while True:
        print("waiting ai task ready, 60s after retry...")
        response = requests.get(url)
        if response.status_code == 200 and response.json()['result_size'] > 0:
            break
        logging.info(response.text)
        time.sleep(60)

    output = os.path.join(current_project_path, 'demo_file', 'demo_output.jpeg')

    images = response.json()['data']

    json_object = json.loads(images)

    base64_to_image(json_object['images'][0], output)
    print("ai task finish: [{}]".format(output))


def image_to_base64(filename):
    with Image.open(filename) as img:
        with BytesIO() as buffer:
            img.save(buffer, 'jpeg')
            return base64.b64encode(buffer.getvalue()).decode()


def base64_to_image(base64_string, filename):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    image.save(filename)

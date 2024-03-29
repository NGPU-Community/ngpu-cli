# -- coding: utf-8 --
import logging
import requests
import time
import json
from .include import GEN_INSTANCE_HOST

# Initiate a task.
def sendTask(video_url, text, btc_address):
    funName = "sendTask"
    logging.info('Function {} video_url={} text={} btc_address={}.'.format(funName, video_url, text, btc_address))
    url = "{}/twinSync/videotalking_v3".format(GEN_INSTANCE_HOST)
    #set https header
    headers = {
        'Content-Type': 'application/json',
    }
    #set https body
    ddata = {
        "video_url": video_url,
        "text": text,
        "btc_address": btc_address,
    }
    #initiate an https request
    try:
        response = requests.post(url, json=data, headers=headers)
        #Print the returned content
        logging.info(json.dumps(response.json(), indent=2))
        #check status code
        if response.status_code == 200:
            taskID = response.json()['task_id']
            logging.info('Function {} Task request initiated, the task ID is taskID={}'.format(funName, taskID))
            return True, taskID
        
        logging.error('Function {} failed: {}'.format(funName, response.json()))
        return False, ''
    except requests.exceptions.Timeout:
        logging.error("the request timed out")
        return False, ''
    except Exception as err:
        logging.exception("Function %s Failed err: %s", funName, err)
        return False, ''

# Query the task status.
def checkTask(taskID):
    funName = "checkTask"
    logging.info('Function {} taskID={}.'.format(funName, taskID))
    url = "{}/twinSync/videotalking_v3?taskID={}".format(GEN_INSTANCE_HOST, taskID)
    #set https header
    headers = {
        'Content-Type': 'application/json',
    }
    #initiate an https request
    try:
        response = requests.get(url, headers=headers)
        #Print the returned content
        logging.info(json.dumps(response.json(), indent=2))
        #check status code
        if response.status_code == 200:
            resultCode = response.json()['result_code']
            logging.info('Function {} Checking the current progress of the task returns, the return value is result_code={}'.format(funName, resultCode))
            return True, resultCode, response.json()['result_url']
        
        logging.error('Function {} failed: {}'.format(funName, response.json()))
        return False, 0, ''
    except requests.exceptions.Timeout:
        logging.error("the request timed out")
        return False, 0, ''
    except Exception as err:
        logging.exception("Function %s Failed err: %s", funName, err)
        return False, 0, ''

def v2v_medium(args):
    """
    cli: main.py v2v_medium
    @:arg: -n/--name <name> -t/--tag <tag> -f/--file <file> -d/--dir <dir>
    """
    funName = "v2v_medium"
    video_url = args.video_url
    text = args.text
    btc_address = args.btc_address

    # Initiate a v2v task.
    logging.info('Gen-Instance {} sendTask->>'.format(funName))
    err, taskId = sendTask(image_url, text, pronouncer, backGroundName, btc_address, logo_url)
    
    #Loop to check the task status.
    if err == True :
        logging.info('Gen-Instance {} sendTask result taskId={}'.format(funName, taskId))

        while True:
            # Every 30 seconds.
            time.sleep(10)

            logging.info('Gen-Instance {} check task state taskId={}'.format(funName, taskId))
            success, resultCode, resultUrl = checkTask(taskId)
            if resultCode == 100 or resultCode == 104 or resultCode == 200:
                logging.info('Function {} Video generation completed, the video address is resultUrl={}'.format(funName, resultUrl))
                return

            logging.info('Gen-Instance {} check task state taskId={} resultCode={}'.format(funName, taskId, resultCode))
    else:
        logging.error('Gen-Instance {} sendTask failed image_url={} text={} pronouncer={} backGroundName={} btc_address={} logo_url={}'.format(funName, image_url, text, pronouncer, backGroundName, btc_address, logo_url))
# -- coding: utf-8 --
import logging
import requests
import time
import json
from .include import GEN_INSTANCE_HOST

''' Startup command: 
    /bin/python3 
    -- /home/fxh7622/ngpu-cli/main.py p2s_medium 
    --image_url https://obai.aimc.digital/20240328170028340811.jpg 
    --text Hello\ everyone,\ I\ am\ AI-generated\ Musk 
    --pronouncer en-US-GuyNeural 
    --backGroundName https://obai.aimc.digital/background/AINN_BG.png 
    --btc_address bc1pp8vyhh2ma0ntzjwr26xxrn5r0w296yu68wdwle5rrhgtv3a2lgkqtyayus'''

# Initiate a task.
def sendTask(image_url, text, pronouncer, backGroundName, btc_address, logo_url):
    funName = "sendTask"
    logging.info('Function {} image_url={} text={} pronouncer={} backGroundName={} btc_address={} logo_url={}.'.format(funName, image_url, text, pronouncer, backGroundName, btc_address, logo_url))
    url = "{}/twinSync/sadTalker".format(GEN_INSTANCE_HOST)
    #set https header
    headers = {
        'Content-Type': 'application/json',
    }
    #set https body
    data = {
        "image_url": image_url,
        "text": text,
        "pronouncer": pronouncer,
        "backGroundName": backGroundName,
        "btc_address": btc_address,
        "logo_url": logo_url,
    }
    #initiate an https request
    try:
        response = requests.post(url, json=data, headers=headers)
        #Print the returned content
        logging.info(json.dumps(response.json(), indent=4))
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
    url = "{}/twinSync/sadTalker?taskID={}".format(GEN_INSTANCE_HOST, taskID)
    #set https header
    headers = {
        'Content-Type': 'application/json',
    }
    #initiate an https request
    try:
        response = requests.get(url, headers=headers)
        #Print the returned content
        logging.info(json.dumps(response.json(), indent=4))
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

def p2s_medium(args):
    """
    cli: main.py p2s_medium
    @:arg: --image_url=<image_url> image cloud address used for making the video
    @:arg: --text=<text> text content used in the video
    @:arg: --pronouncer=<pronouncer> speaker used in the video
    @:arg: --backGroundName=<backGroundName> background used in the video
    @:arg: --btc_address=<btc_address> BTC address (used to check for AINN and other BRC20 assets
    @:arg: --logo_url=<logo_url> logo cloud address used in the video
    """
    funName = "p2s_medium"
    image_url = args.image_url
    text = args.text
    pronouncer = args.pronouncer
    backGroundName = args.backGroundName
    btc_address = args.btc_address
    logo_url = args.logo_url

    # Initiate a p2s task.
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
                logging.info('Function {} Video generation completed taskId={} the video address is resultUrl={}'.format(funName, taskId, resultUrl))
                return

            logging.info('Gen-Instance {} check task state taskId={} resultCode={}'.format(funName, taskId, resultCode))
    else:
        logging.error('Gen-Instance {} sendTask failed image_url={} text={} pronouncer={} backGroundName={} btc_address={} logo_url={}'.format(funName, image_url, text, pronouncer, backGroundName, btc_address, logo_url))
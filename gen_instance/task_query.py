# -- coding: utf-8 --
import logging
import requests
import time
import json
from .include import GEN_INSTANCE_HOST

''' Startup command: 
    /bin/python3 
    -- /home/fxh7622/ngpu-cli/main.py task_query 
    --taskID 20240329_09_37_16_458230'''

# Query the task information.
def queryTask(taskID):
    funName = "queryTask"
    logging.info('Function {} taskID={}.'.format(funName, taskID))
    url = "{}/user/getTask?taskID={}".format(GEN_INSTANCE_HOST, taskID)
    #set https header
    headers = {
        'Content-Type': 'application/json',
    }
    logging.info('{} Query Task information url={}'.format(funName, url))

    #initiate an https request
    try:
        response = requests.get(url, headers=headers)

        #check status code
        if response.status_code == 200:
            return True, response.json()
        
        logging.error('Function {} failed: {}'.format(funName, response.json()))
        return False, ''

    except requests.exceptions.Timeout:
        logging.error("the request timed out")
        return False, "the request timed out"

    except Exception as err:
        logging.exception("Function %s Failed err: %s", funName, err)
        return False, err

def task_query(args):
    """
    cli: main.py task_query
    @:arg: --taskID=<taskID> The task ID that needs to be queried
    """
    funName = "task_query"
    taskID = args.taskID

    logging.info('{} Query Task information taskID={}'.format(funName, taskID))
    success, resBody = queryTask(taskID)
    if success:
        formatted_json = json.dumps(resBody, indent=4)
        logging.info('{} Query Task information taskID={} \n resBody={}'.format(funName, taskID, formatted_json))
        return

    logging.error('{} Query Task information Failed taskID={} \n error={}'.format(funName, taskID, resBody))

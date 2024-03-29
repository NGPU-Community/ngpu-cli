# -- coding: utf-8 --
import logging
import requests
import time
import json
from .include import GEN_INSTANCE_HOST

# Query the task information.
def queryTask(taskID):
    funName = "queryTask"
    logging.info('Function {} taskID={}.'.format(funName, taskID))
    url = "{}/manager/getTask?taskID={}".format(GEN_INSTANCE_HOST, taskID)
    #set https header
    headers = {
        'Content-Type': 'application/json',
    }
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
    @:arg: -n/--name <name> -t/--tag <tag> -f/--file <file> -d/--dir <dir>
    """
    funName = "task_query"
    taskID = args.taskID

    logging.info('{} Query Task information taskID={}'.format(funName, taskID))
    success, resBody = queryTask(taskID)
    if success:
        formatted_json = json.dumps(resBody, indent=2)
        logging.info('{} Query Task information taskID={} \n resBody={}'.format(funName, taskID, formatted_json))
        return

    logging.error('{} Query Task information Failed taskID={} \n error={}'.format(funName, taskID, resBody))

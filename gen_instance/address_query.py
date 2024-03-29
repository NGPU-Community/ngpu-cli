# -- coding: utf-8 --
import logging
import requests
import time
import json
from .include import GEN_INSTANCE_HOST

''' Startup command: 
    /bin/python3 
    -- /home/fxh7622/ngpu-cli/main.py address_query 
    --btcaddress bc1pp8vyhh2ma0ntzjwr26xxrn5r0w296yu68wdwle5rrhgtv3a2lgkqtyayus'''

# Query the task information.
def queryTasks(btcaddress):
    funName = "queryTasks"
    logging.info('Function {} btcaddress={}.'.format(funName, btcaddress))
    url = "{}/manager/getTasks?btcaddress={}".format(GEN_INSTANCE_HOST, btcaddress)
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

def address_query(args):
    """
    cli: main.py task_query
    @:arg: --btcaddress=<btcaddress> User BTC address required for query
    """
    funName = "address_query"
    btcaddress = args.btcaddress

    logging.info('{} Query task list based on the user BTC address btcaddress={}'.format(funName, btcaddress))
    success, resBody = queryTasks(btcaddress)
    if success:
        formatted_json = json.dumps(resBody, indent=4)
        logging.info('{} Query Task information btcaddress={} \n resBody={}'.format(funName, btcaddress, formatted_json))
        return

    logging.error('{} Query Task information Failed btcaddress={} \n error={}'.format(funName, btcaddress, resBody))

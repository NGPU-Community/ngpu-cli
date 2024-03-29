# -- coding: utf-8 --
import logging
import requests
from .include import GEN_INSTANCE_HOST

def i2i_medium(args):
    """
    cli: main.py v2v_medium
    @:arg: -n/--name <name> -t/--tag <tag> -f/--file <file> -d/--dir <dir>
    """
    audio_url = args.audio_url
    video_url = args.video_url
    btc_address = args.btc_address

    url = "{}/twinSync/videotalking".format(GEN_INSTANCE_HOST)

    #set https header
    headers = {
        'Content-Type': 'application/json',
    }

    #set https body
    data = {
        "audio_url": audio_url,
        "video_url": video_url,
        "btc_address": btc_address,
    }

    #initiate an https request
    try:
        response = requests.post(url, json=data, headers=headers)

        #Print the returned content
        logging.info(response.json())

        #check status code
        if response.status_code == 200:
            logging.info('v2v_medium result: image id[{}]'.format(response.json()['result']['image_id']))
            return
        
        logging.error('v2v_medium failed: {}'.format(response.json()))
    except requests.exceptions.Timeout:
        logging.error("the request timed out")
    except Exception as err:
        raise err



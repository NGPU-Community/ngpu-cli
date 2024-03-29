# -- coding: utf-8 --
import requests
import logging
import json

backend_url = "https://gslb.ipolloverse.cn"
#based on https://github.com/AINNGPU-Community/ngpu-schedule

def node_new_account(args) -> str:
    """
    cli: create a new node address
    """
    cmd_url = "/user/newAccount"

    response = requests.get(backend_url + cmd_url)
    effectiveStr = json.dumps(response.json(), indent=4)
    logging.info(f"for new account, return \n {effectiveStr}")
    return effectiveStr


def node_register_node(args) -> str:
    """
    cli: register node address to user wallet account, so use can get incentive from the node
    """
    headers = {
        'Content-Type': 'application/json'
    }
    cmd_url = "/user/nodeRegister"
    postParam = {"nodeAddr":args.node_addr,
                 "orgName": args.organization,
                 "walletAccount":args.wallet_account}
    response = requests.post(backend_url + cmd_url, json = postParam, headers=headers)
    effectiveStr = json.dumps(response.json(), indent=4)
    logging.info(f'for register node, return \n{effectiveStr}')
    return effectiveStr


def node_query_all_nodes(args) -> str:
    """
    cli: get all the node info
    """

    cmd_url = "/user/getNodes"
    response = requests.get(backend_url + cmd_url)
    effectiveStr = json.dumps(response.json(), indent=4)    
    logging.info(f"for getNodes, return {effectiveStr}")
    return effectiveStr


def node_query_node(args) -> str:
    """
    cli: get one node info, specified by node address
    """
    cmd_url = "/user/getNode?nodeAddr=" + args.node_addr
    response = requests.get(backend_url + cmd_url)
    effectiveStr = json.dumps(response.json(), indent=4)
    logging.info(f"for getNode for address = {args.node_addr}, return \n {effectiveStr}")
    return effectiveStr

def node_query_node_incentive(args) -> str:
    """
    cli: get incentive info of one node, specified by node address
    """
    cmd_url = "/user/getBalance"
    headers = {
        'Content-Type': 'application/json'
    }
    postParam = {"nodeAddrs":[args.node_addr]}

    response = requests.post(backend_url + cmd_url, json = postParam, headers=headers)
    
    effectiveStr = json.dumps(response.json(), indent=4)
    logging.info(f'for get balance (incentive), return  {effectiveStr}')
    return effectiveStr
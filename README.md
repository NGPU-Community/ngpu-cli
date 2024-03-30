NGPU-Cli
=======
python cmd for ngpu main api calls.
-----------

## Features

```
1. calculation node: 
.New address (node_new_account), 
.Bind node address with wallet address (node_register_node)
.After this, please install ngpu client with node address from node_new_account by install script from https://github.com/AINNGPU-Community/ngpu-installation, To uninstall node, please run uninstall script. 
.Query all the nodes in network, including inactive and active ones (node_query_all_nodes)
.Query node info by node address (node_query_node)
.Query node incentive info by node address. when node address has been registered to one wallet, no incentive left at node address, so return 0. In that case, use wallet address to get all the incentives from all registered nodes.(node_query_node_incentive)

```

## Notes

* [Running module](#Running)
    * [Node cmd part](#Node-cmd-introduction): If you want to provide GPU for NGPU, read this note
    * [Cloud cmd part](#Cloud-cmd-introduction): If you want to use the GPU computing power in NGPU, read this note
    * [Caller cmd part](): If you want to call AI on NGPU, read this note

## Installing

```
Python environment is 3.12, so run python -V, return 3.12
To install packages, please pip install -r requirements.txt 
```

## Running

- cmd example:

```
python --help, it returns all the parameters and descriptions. 
python main.py version
python main.py cloud-image-create --name=<image name string> --wget-url=<docker tar wget url> --start=<docker run string> --docker-image-id=<docker image id>
python main.py cloud-image-list

For node part, the following cmd
python main.py new-account
python main.py register-node --node-addr 14d5459d13f16cadae01cc3acb8d97a4721e3652 --organization whoami --wallet-account 0xdc49c76d46ba35802013400d5d98e5fb8486d01f  ### node-addr is from new account. 
python main.py query-all-nodes  
python main.py query-node --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
python main.py query-node-incentive --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13   ### this is node address, and this node has been registered to wallet address, so cmd returns 0.
python main.py query-node-incentive --node-addr 0xdc49c76d46ba35802013400d5d98e5fb8486d01f   ### this is wallet address, all incentives from all nodes. 
```

### Node cmd introduction

🎉 Follow the steps, you can join the network and get incentives

#### Node join NGPU network

##### 1. Create New account

```
$ python main.py new-account

return:  
{
    "passWD": "888888",
    "fileName": "0xf942f1adc3bfc57cf075476236eee476199e853a_keystroe.json",
    "keystore": "{\"address\":\"f942f1adc3bfc57cf075476236eee476199e853a\",\"crypto\":{\"cipher\":\"aes-128-ctr\",\"ciphertext\":\"01993647630f506ed08a0897a2d5b9c070cd4d26da4178e27fa8c222ea25c2ee\",\"cipherparams\":{\"iv\":\"de459d6d742cdcfd49311a2bcc224777\"},\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":262144,\"p\":1,\"r\":8,\"salt\":\"3090949f8ca9e51f9a82abcbcd0f994f65367b399e86bc7d59b62f647e85dc5a\"},\"mac\":\"cf6e1997a3c62d7e47b5c414be5f4f20330d2ce77279024cd9fa5673df4f4532\"},\"id\":\"3010e90c-4478-42d3-b8ef-79ddd0cadd3a\",\"version\":3}"
}
```

Return:

- address: The node address you applied for is used as the registered node

##### 2.  register node

```
$ python main.py register-node
    --node-addr=<new-account return address>
    --organization=<customize by yourself>
    --wallet-account=<your eth address>
```

Parameter:

- node-addr: from new-account return
- organization: customize by yourself
- wallet-account: your eth address(incentive address), not node-address,

##### 3. Go to PC and install node client

- [node client install](https://github.com/AINNGPU-Community/ngpu-install-script)
- You may need to wait for the network to measure your PC after installation

##### 4. Get node information

```
python main.py query-all-nodes  
python main.py query-node --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
python main.py query-node-incentive --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
```

### Cloud cmd introduction

Follow the steps below to use GPU computing power on the network for your own AI programs:

#### Case1: create workspace for image when you have the required parameter

```
$ python main.py cloud-workspace-create --name=<workspace name for yourself> \
    --image-id=<one of cloud-image-list return> \
    --product-id=<one of cloud-product-list> \
    --unit=<one of "hr" or "week" or "month"> \
    --duration=<int> \
    --node-num=<int> \
    --is-group=<true or false>
    --group-id=<one of cloud-workspace-group-list return>
    
return: workspace id [<str>]
```

Parameter:

- name: required. The name of the created workspace, unique.
- image-id: required. From cloud-image-list cmd, return id in json map item. If you want to create image, refer to
  cloud-image-create cmd.
- product-id: required. From cloud-product-id, return product id in json map item. Choose you need GPU type.
- unit: required. Duration unit include `hr`(pre hour), `week`(pre week), `month`(pre month).
- duration: required. You want to use GPU time.
- node-num: required. You want to use node num.
- is-group: default `false`, if node-num > 1, it is `true`.
- group-id: if is-group is `true`, setting it. From cloud-workspace-group-list cmd return group id in json map item.

* Get workspace id

* [Please review the next steps](#5-check-workspace-status)

#### Case2: Build parameter when you don't have anything.

##### 1. image

###### 1.1 create image

```
$ python main.py cloud-image-create --name="xxx" \
    --name=<str>
    --wget-url=<str>
    --note=<str>
    --start=<str>
    --ports=<str>
    --docker-image-id=<str>
 
return: image id [312243674765329408]
```

Parameter:

- name: required. The name of the created image, unique.
- wget-url: required. download docker tar file url.
- note: this image description.
- start: required. Docker run cmd.
- ports: required. Docker run ports param.
- docker-image-id: Docker image id from `$ docker images` info.

Return:
- image id: used in cloud-workspace-create

###### 1.2 image list of creating history (ignorable)

```
$ python main.py cloud-image-list
 
return: 
[
    {
        "id": "312243674765329408",
        "image_name": "stable diffusion",
        "file_size": 18022273024,
        "created_at": "2023-07-20 11:37:11",
        "note": "stable diffusion standard version, containing SD 1.5 model",
        "action": 1,
        "start_cmd": "docker run -d --gpus all  -p 7860:7860 e795e95b9616 /data/stable-diffusion-webui/webui.sh --listen --api",
        "stop_cmd": "",
        "port_mapping": "7860:7860",
        "exception": 1,
        "is_system": true,
        "docker_image_id": "e795e95b9616"
    },
    ...
]
```

* Get image id for `cloud-workspace-create --image-id` parameter

##### 2. group

###### 2.1 create group

```
$ python main.py cloud-workspace-group-create --name="xxx"
    
return: workspace group id [312243674765329408]
```

###### 2.2 group list of creating history (ignorable)

```
$ python main.py cloud-workspace-group-list

return:
[
    {
        "id": "362502199797875713",
        "workspace_group_name": "testgroup"
    },
    {
        "id": "362502199797875714",
        "workspace_group_name": "aaa"
    }
]
```

* Get group id for `cloud-workspace-create --group-id` parameter

##### 3. product

###### 3.1 product list

```
$ python main.py cloud-product-list

return:
[
    {
        "id": 10,
        "product_name": "PGPU-3090-24G-nCN",
        "gpu_name": "NVIDIA GeForce RTX 3090",
        "gpu_type": "NVIDIA GeForce RTX",
        "gpu_model": "3090",
        "video_memory": 24,
        "core_num": 16,
        "memory": 64,
        "storage": 1000,
        "net_band": 50,
        "operating_system": "Ubuntu20.04LTS x64",
        "hour_price": 0.28,
        "month_price": 157,
        "week_price": 280,
        "area": "!CN",
        "description": "3090 out of China"
    }
]
```

* return: Available gpu specs info.
* Get product id for `cloud-workspace-create --product-id` parameter

##### 4. Create workspace

- [Case 1](#case1-create-workspace-for-image-when-you-have-the-required-parameter)


##### 5. Check workspace status

```
$ python main.py cloud-workspace-dispense-status --id="xxx"

return: workspace: id: [xxx], name: [xxx] dispense success
```

##### 6. Scheduling URL

- Wait workspace dispense success

```

POST https://xxxx

header {
  WorkspaceId: ""
}
```

## QA


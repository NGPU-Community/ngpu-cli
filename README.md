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
python main.py cloud-image-create cloud-image-create --name=cmdtest --wget-url="https://xxxx" --start="docker run -d --gpus all -p 7861:80 -p 7871:22 021283c8eb95" --ports="80:80" --docker-image-id="021283c8eb95"
python main.py cloud-image-list

For node part, the following cmd
python main.py new-account
python main.py register-node --node-addr 14d5459d13f16cadae01cc3acb8d97a4721e3652 --organization whoami --wallet-account 0xdc49c76d46ba35802013400d5d98e5fb8486d01f  ### node-addr is from new account. 
python main.py query-all-nodes  
python main.py query-node --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
python main.py query-node-incentive --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13   ### this is node address, and this node has been registered to wallet address, so cmd returns 0.
python main.py query-node-incentive --node-addr 0xdc49c76d46ba35802013400d5d98e5fb8486d01f   ### this is wallet address, all incentives from all nodes. 
```

### Cloud cmd introduction

To obtain the final scheduling address, you need to perform the following steps:

#### Case1: create workspace for image when you have the required parameter

```
$ python main.py cloud-workspace-create --name="xxx" \
    --image-id="xxx" \
    --product-id="xxx" \
    --unit="hr" \
    --duration=10 \
    --node-num=1 \
    --is-group=false
    --group-id="xxx"
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

#### Case2: Build parameter when you don't have anything.

##### 1. image  
###### 1.1 create image
```
$ python main.py cloud-image-create --name="xxx" \
    --name="xxx"
    --wget-url="https://xxx"
    --note="xxx"
    --start="xxx"
    --ports="xxx"
    --docker-image-id="xxx"
 
return: image id [312243674765329408]
```

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

4. Create workspace

- [Case 1](#case1-create-workspace-for-image-when-you-have-the-required-parameter)


5. Check workspace status

```
$ python main.py cloud-workspace-dispense-status --id="xxx"

return: workspace: id: [xxx], name: [xxx] dispense success
```

6. Scheduling URL

```

POST https://xxxx

header {
  WorkspaceId: ""
}
```





## Notes

## QA


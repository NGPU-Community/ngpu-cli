NGPU-Cli
=======
python cmd for ngpu main api calls.
-----------

## Features

```shell
1. calculation node: 
.New address (node_new_account), 
.Bind node address with wallet address (node_register_node)
.After this, please install ngpu client with node address from node_new_account by install script from https://github.com/AINNGPU-Community/ngpu-installation, To uninstall node, please run uninstall script. 
.Query all the nodes in network, including inactive and active ones (node_query_all_nodes)
.Query node info by node address (node_query_node)
.Query node incentive info by node address. when node address has been registered to one wallet, no incentive left at node address, so return 0. In that case, use wallet address to get all the incentives from all registered nodes.(node_query_node_incentive)

```

## Notes

* [General Commands](#General-Commands)If you're looking for general script commands, read this note.
* [**Node part**](#Node-part): If you want to provide GPU for NGPU, read this note
* [**Cloud part**](#Cloud-part): If you want to use the GPU computing power in NGPU, read this note
* [**Caller part**](#Caller-part): If you want to call AI on NGPU, read this note

## Installing

```shell
Python environment is 3.12, so run python -V, return 3.12
To install packages, please pip install -r requirements.txt 
```

### General Commands

```shell
$ python3 main.py version
```
cmd Name | Command Explanation
----|:----:|
version|Get the current script version information.


## **Node part**: 

### Command Line Example and Explanation

#### 1.  **new-account**
```shell
$ python3 main.py new-account
```
Command Explanation：
- Create a computational power node address (this address uses an ETH address, so ETH addresses obtained through other means can also be used).

Response:
```shell
{
    "passWD": "888888",
    "fileName": "0xf942f1adc3bfc57cf075476236eee476199e853a_keystroe.json",
    "keystore": "{\"address\":\"f942f1adc3bfc57cf075476236eee476199e853a\",\"crypto\":{\"cipher\":\"aes-128-ctr\",\"ciphertext\":\"01993647630f506ed08a0897a2d5b9c070cd4d26da4178e27fa8c222ea25c2ee\",\"cipherparams\":{\"iv\":\"de459d6d742cdcfd49311a2bcc224777\"},\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":262144,\"p\":1,\"r\":8,\"salt\":\"3090949f8ca9e51f9a82abcbcd0f994f65367b399e86bc7d59b62f647e85dc5a\"},\"mac\":\"cf6e1997a3c62d7e47b5c414be5f4f20330d2ce77279024cd9fa5673df4f4532\"},\"id\":\"3010e90c-4478-42d3-b8ef-79ddd0cadd3a\",\"version\":3}"
}
```
Parameter:
- --passWD: Create a generated keystore password
- --fileName: Create a generated keystore file name
- --keystore: Create the content of the generated keystore file

#### 2. **register-node**
```shell
$ python3 main.py register-node --node-addr < Computational Power Node Address > --organization < Organization Name > --wallet-account < Wallet Address >
```
Command Explanation:
- Register a computational power node on AINNGPU

Parameter:
- --node-addr: from new-account return
- --organization: customize by yourself
- --wallet-account: your eth address(incentive address), not node-address

#### 3. **query-all-nodes**
```shell
$ python3 main.py query-all-nodes 
```
Command Explanation:
- Query all current computational power nodes


#### 4. **query-node**
```shell
$ python3 main.py query-node --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
```
Command Explanation:
- Retrieve detailed information of a computational power node based on its address

Parameter:
- --node-addr: The computational power node address you need to query

#### 5. **query-node-incentive**
```shell
$ python3 main.py query-node-incentive --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
```
Command Explanation:
- Query all current computational power nodes

Parameter:
- --node-addr: The computational power node address you need to query


### **_Operation Steps_**
1. **Step One**: Create a computational power node address (you can skip this step if you already have an ETH address).
```shell
$ python3 main.py new-account
```
<span style="color:red;"> Assuming the returned address is: 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 </span>

2. **Step Two**: Register the computational power node address with the AINNGPU platform.
```shell
$ python3 main.py query-node --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13 
```
3. **Step Three**: Run the computational power node installation script
- [node client install](https://github.com/AINNGPU-Community/ngpu-install-script)
- You may need to wait for the network to measure your PC after installation

4. **Step Four**: Query the incentive amount received by the computational power node
```shell
$ python3 main.py query-node-incentive --node-addr 0x732637A3A3E0D335Dc00d9F8fba8a1033831Bf13
```

## Cloud part

### Command Line Example and Explanation

#### 1. create workspace
```shell
$ python3 main.py cloud-workspace-create --name=< workspace name for yourself > \
    --image-id=< one of cloud-image-list return > \
    --product-id=< one of cloud-product-list > \
    --unit=< one of "hr" or "week" or "month" > \
    --duration=< int > \
    --node-num=< int > \
    --is-group=< true or false >
    --group-id=< one of cloud-workspace-group-list return >
```
Command Explanation:
- Create a workspace

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

Response:
- workspace id [<str>]


#### 2. create image

```shell
$ python3 main.py cloud-image-create --name=<str> \
    --name=<str>
    --wget-url=<str>
    --note=<str>
    --start=<str>
    --ports=<str>
    --docker-image-id=<str>
```
Response:
- image id [<str>]

Parameter:

- name: required. The name of the created image, unique.
- wget-url: required. download docker tar file url.
- note: this image description.
- start: required. Docker run cmd.
- ports: required. Docker run ports param.
- docker-image-id: Docker image id from `$ docker images` info.

Response:
- image id: used in cloud-workspace-create

#### 3. image list 
```shell
$ python3 main.py cloud-image-list
 ```


Response:
```shell
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
Parameter:
- id: imageid used cloud-workspace-create.
- image_name: image name
- docker_image_id: docker image id from `$ docker images` info.
- start_cmd: docker run cmd.
- port_mapping: docker run --ports param.

* <span style="color:green;"> **_Get image id for `cloud-workspace-create --image-id` parameter_** </span>


#### 4. create group

```shell
$ python main.py cloud-workspace-group-create --name=<str>
```

Response:
- workspace group id [<str>]

Parameter:
- name: required, unique. The name of the created.

#### 5. group list

```shell
$ python3 main.py cloud-workspace-group-list
```
Response:
```shell
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
Parameter:
- id: group id used cloud-workspace-create
- workspace_group_name: unique, group name

* <span style="color:green;"> **_Get group id for `cloud-workspace-create --group-id` parameter_** </span>


#### 6. product list

```shell
$ python3 main.py cloud-product-list
```
Response:
```shell
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
Parameter:
- id: <span style="color:green;"> **_product id for `cloud-workspace-create --product-id` parameter_**</span>
- gpu_name: gpu name
- operating_system: os
- hour_price: price per hour
- week_price: price per week
- month_price: price per month

#### 7. check workSpace status

```shell
$ python3 main.py cloud-workspace-dispense-status
```
Response:
```shell
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
Parameter:
- id: <span style="color:green;"> **_product id for `cloud-workspace-create --product-id` parameter_**</span>
- gpu_name: gpu name
- operating_system: os
- hour_price: price per hour
- week_price: price per week
- month_price: price per month


### **_Operation Steps_**
1. **Step One**: Create a workspace.
```shell
$ python3 main.py cloud-workspace-create --name=<workspace name for yourself> \
    --image-id=< one of cloud-image-list return > \
    --product-id=< one of cloud-product-list > \
    --unit=< one of "hr" or "week" or "month" > \
    --duration=< int > \
    --node-num=< int > \
    --is-group=< true or false >
    --group-id=< one of cloud-workspace-group-list return >
```
 - <span style="color:red;"> **_When you don't know the image-id parameter, you can use the cloud-image-list command to obtain it or use the cloud-image-create command to create a new image_**. </span>
 - <span style="color:red;"> **_When you don't know the product-id parameter, you can use the cloud-product-list command to obtain it_**. </span>
 - <span style="color:red;"> **_When you don't know the group-id parameter, you can use the cloud-workspace-group-list command to obtain it or use the cloud-workspace-group-create command to create a new group_**. </span>


2. **Step Two**: Check the distribution status of your workspace.
```shell
$ python3 main.py cloud-workspace-dispense-status --id=<str>
```
Parameter:
- id: The workspace ID obtained through the cloud-workspace-create command


## Caller part

### Command Line Example and Explanation

#### 1. **create p2s_medium**

```shell
$ python3 main.py p2s_medium --image_url=<str> --text=<str> --pronouncer=<str> --btc_address=<str> --logo_url=<str>
```
Command Explanation:
- Generate a video using photos.

Parameter:
- --image_url: URL Address of the Image
- --text: Spoken Content in the Video
- --pronouncer：Speaker used in the video
- --btc_address：BTC address (used to check for AINN and other BRC20 assets)
- --logo_url：Logo cloud address used in the video

#### 2. **task_query**

```shell
$ python3 main.py task_query  --taskID=<str>
```
Command Explanation:
- Get detailed information about the task based on its task ID.

Parameter:
- --taskID: Task ID

### **_Operation Steps_**
1. **Step One**: Generate a video from photos using an AI interface.
```shell
$ python3 main.py p2s_medium --image_url https://obai.aimc.digital/20240328170028340811.jpg --text Hello\ everyone,\ I\ am\ AI-generated\ Musk --pronouncer en-US-GuyNeural --backGroundName https://obai.aimc.digital/background/AINN_BG.png --btc_address bc1pp8vyhh2ma0ntzjwr26xxrn5r0w296yu68wdwle5rrhgtv3a2lgkqtyayus
```
<span style="color:red;">Return the task ID and the URL address of the generated video </span>

2. **Step Two**: Query the detailed information of the task after execution
```shell
$ python3 main.py task_query --taskID 20240329_09_37_16_458230 
```


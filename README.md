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
## Notes



## QA


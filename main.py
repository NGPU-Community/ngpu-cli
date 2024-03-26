import argparse

from cli import version, cloud_image_create, cloud_image_list

from cli import node

def version_cmd(subparsers: any) -> None:
    # "version" command
    sub_parser = subparsers.add_parser('version', help='ngpu-cli version')
    # parser_image_create.add_argument('integers', metavar='N', type=int, nargs='+',
    #                                  help='an integer for the accumulator')
    sub_parser.set_defaults(func=version.version)


def cloud_image_create_cmd(subparsers: any) -> None:
    # TODO add child parser for the "sum" command
    sub_parser = subparsers.add_parser('cloud-image-create', help='create docker image info, return image id')
    sub_parser.add_argument('--name', type=str, help='docker image name', required=True)
    sub_parser.add_argument('--wget-url', type=str, help='wget url download', required=True)
    sub_parser.add_argument('--note', type=str, help='description')
    sub_parser.add_argument('--start', type=str, help='docker run command', required=True)
    sub_parser.add_argument('--ports', type=str, help='docker ports mapping')
    sub_parser.add_argument('--docker-image-id', type=str, help='docker image id', required=True)
    sub_parser.set_defaults(func=cloud_image_create.cloud_image_create)


def cloud_image_list_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-image-list', help='list docker images')
    sub_parser.set_defaults(func=cloud_image_list.cloud_image_list)

#####for node actions by Edward
#no input param, output is node Address
def node_new_account(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('new-account', help='create one new node address')
    sub_parser.set_defaults(func=node.node_new_account)

#register the node to user's account
def node_register_node(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('register-node', help='register node address to user wallet account, so use can get incentive from the node')
    sub_parser.add_argument('--node-addr', help='Computer Node Address')
    sub_parser.add_argument('--organization', help='Computer Node Organization Name')
    sub_parser.add_argument('--wallet-account', help='User Account (Ethereum address type)')
    sub_parser.set_defaults(func=node.node_register_node)

#get all the node info
def node_query_all_nodes(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('query-all-nodes', help='get all the node info')
    sub_parser.set_defaults(func=node.node_query_all_nodes)

#get get one node info, specified by node address
def node_query_node(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('query-node', help='get one node info, specified by node address')
    sub_parser.add_argument('--node-addr', help='Computer Node Address')
    sub_parser.set_defaults(func=node.node_query_node)

#get get incentive info of one node, specified by node address
def node_query_node_incentive(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('query-node-incentive', help='get incentive info of one node, specified by node address')
    sub_parser.add_argument('--node-addr', help='Computer Node Address')
    sub_parser.set_defaults(func=node.node_query_node_incentive)

if __name__ == '__main__':
    # create main parser
    parser = argparse.ArgumentParser(prog='NGPU', description='NGPU Cli')
    subparsers = parser.add_subparsers(help='NGPU Cli')

    # version cli
    version_cmd(subparsers=subparsers)

    # cloud-* cli
    cloud_image_create_cmd(subparsers=subparsers)
    cloud_image_list_cmd(subparsers=subparsers)

    #node -> cli
    node_new_account(subparsers=subparsers)
    node_register_node(subparsers=subparsers)
    
    #node_enroll_node(subparsers=subparsers)  #in installation script
    #node_disconnect_node(subparsers=subparsers)  #in uninstallation script

    node_query_all_nodes(subparsers=subparsers)
    node_query_node(subparsers=subparsers)
    node_query_node_incentive(subparsers=subparsers)

    # end
    args = parser.parse_args()
    args.func(args)

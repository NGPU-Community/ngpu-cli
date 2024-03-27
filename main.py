import argparse

from cli import version, cloud_image_create, cloud_image_list, cloud_workspace_list, cloud_product_list, \
    cloud_workspace_create

from cli import node


def version_cmd(subparsers: any) -> None:
    # "version" command
    sub_parser = subparsers.add_parser('version', help='ngpu-cli version')
    # parser_image_create.add_argument('integers', metavar='N', type=int, nargs='+',
    #                                  help='an integer for the accumulator')
    sub_parser.set_defaults(func=version.version)


def cloud_image_create_cmd(subparsers: any) -> None:
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


def cloud_workspace_create_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-workspace-create', help='create workspace info, return workspace info')
    sub_parser.add_argument('--name', type=str, help='docker image name', required=True)
    sub_parser.add_argument('--image-id', type=str, help='cloud-image-list return image id', required=True)
    sub_parser.add_argument('--product-id', type=str, help='cloud-product-list return product id', required=True)
    sub_parser.add_argument('--node-num', type=int, help='need node num, if > 1, need do group', default=1)
    sub_parser.add_argument('--unit', type=str, help='need duration unit: hr, week, month', default="month")
    sub_parser.add_argument('--duration', type=int, help='need duration', default=1)
    sub_parser.set_defaults(func=cloud_workspace_create.cloud_workspace_create)


def cloud_workspace_list_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-workspace-list', help='list workspace')
    sub_parser.add_argument('--id', type=str, help='workspace id')
    sub_parser.set_defaults(func=cloud_workspace_list.cloud_workspace_list)


def cloud_product_list_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-product-list', help='list product')
    sub_parser.set_defaults(func=cloud_product_list.cloud_product_list)


#####for node actions by Edward
# no input param, output is node Address
def node_new_account(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('new-account', help='create one new node address')
    sub_parser.set_defaults(func=node.node_new_account)


# register the node to user's account
def node_register_node(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('register-node',
                                       help='register node address to user wallet account, so use can get incentive from the node')
    sub_parser.add_argument('--node-addr', help='Computer Node Address')
    sub_parser.add_argument('--organization', help='Computer Node Organization Name')
    sub_parser.add_argument('--wallet-account', help='User Account (Ethereum address type)')
    sub_parser.set_defaults(func=node.node_register_node)


# get all the node info
def node_query_all_nodes(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('query-all-nodes', help='get all the node info')
    sub_parser.set_defaults(func=node.node_query_all_nodes)


# get get one node info, specified by node address
def node_query_node(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('query-node', help='get one node info, specified by node address')
    sub_parser.add_argument('--node-addr', help='Computer Node Address')
    sub_parser.set_defaults(func=node.node_query_node)


# get get incentive info of one node, specified by node address
def node_query_node_incentive(subparsers: any) -> str:
    sub_parser = subparsers.add_parser('query-node-incentive',
                                       help='get incentive info of one node, specified by node address')
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
    cloud_workspace_create_cmd(subparsers=subparsers)
    cloud_workspace_list_cmd(subparsers=subparsers)
    cloud_product_list_cmd(subparsers=subparsers)

    # node -> cli
    node_new_account(subparsers=subparsers)
    node_register_node(subparsers=subparsers)

    # node_enroll_node(subparsers=subparsers)  #in installation script
    # node_disconnect_node(subparsers=subparsers)  #in uninstallation script

    node_query_all_nodes(subparsers=subparsers)
    node_query_node(subparsers=subparsers)
    node_query_node_incentive(subparsers=subparsers)

    # end
    args = parser.parse_args()
    args.func(args)

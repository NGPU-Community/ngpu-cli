import argparse

from cli import version, cloud_image_create, cloud_image_list, cloud_workspace_list, cloud_product_list, \
    cloud_workspace_create, cloud_workspace_group_create, cloud_workspace_group_list, cloud_workspace_dispense_status

from cli import node
from gen_instance import p2s_medium, task_query, address_query


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
    sub_parser.add_argument('--name', type=str, help='workspace name', required=True)
    sub_parser.add_argument('--image-id', type=str, help='cloud-image-list return image id', required=True)
    sub_parser.add_argument('--product-id', type=str, help='cloud-product-list return product id', required=True)
    sub_parser.add_argument('--unit', type=str, help='need duration unit: hr, week, month', default="month")
    sub_parser.add_argument('--duration', type=int, help='need duration', default=1)
    sub_parser.add_argument('--node-num', type=int, help='need node num, if > 1, need do group', default=1)
    sub_parser.add_argument('--is-group', type=bool, help='if group, need group id param', default=False)
    sub_parser.add_argument('--group-id', type=str, help='cloud-workspace-group-list return group id')

    sub_parser.set_defaults(func=cloud_workspace_create.cloud_workspace_create)


def cloud_workspace_list_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-workspace-list', help='list workspace')
    sub_parser.add_argument('--id', type=str, help='workspace id')
    sub_parser.set_defaults(func=cloud_workspace_list.cloud_workspace_list)


def cloud_workspace_group_create_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-workspace-group-create', help='create workspace group for many nodes')
    sub_parser.add_argument('--name', type=str, help='cloud-image-list return image id', required=True)
    sub_parser.set_defaults(func=cloud_workspace_group_create.cloud_workspace_group_create)


def cloud_workspace_dispense_status_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-workspace-dispense-status', help='workspace dispense status')
    sub_parser.add_argument('--id', type=str, help='workspace id', required=True)
    sub_parser.set_defaults(func=cloud_workspace_dispense_status.cloud_workspace_dispense_status)


def cloud_workspace_group_list_cmd(subparsers: any) -> None:
    sub_parser = subparsers.add_parser('cloud-workspace-group-list', help='list workspace group')
    sub_parser.add_argument('--id', type=str, help='workspace group id')
    sub_parser.set_defaults(func=cloud_workspace_group_list.cloud_workspace_group_list)


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


#####for gen-instance actions by Ethan
def geninstence_p2s(subparsers: any) -> None:
    # Increase parameter calls for the Gen-Instance p2s_medium interface
    sub_parser = subparsers.add_parser('p2s_medium', help='gen_instance p2s_medium')
    sub_parser.add_argument('--image_url', type=str, help='image cloud address used for making the video',
                            required=True)
    sub_parser.add_argument('--text', type=str, help='text content used in the video', required=True)
    sub_parser.add_argument('--pronouncer', type=str, help='speaker used in the video', required=True)
    sub_parser.add_argument('--backGroundName', type=str, help='background used in the video', required=True)
    sub_parser.add_argument('--btc_address', type=str,
                            help='BTC address (used to check for AINN and other BRC20 assets', required=True)
    sub_parser.add_argument('--logo_url', type=str, help='logo cloud address used in the video')
    sub_parser.set_defaults(func=p2s_medium.p2s_medium)


def geninstence_taskQuery(subparsers: any) -> None:
    # Increase parameter calls for the Gen-Instance task query interface
    sub_parser = subparsers.add_parser('task_query', help='gen_instance task information query')
    sub_parser.add_argument('--taskID', type=str, help='The task ID that needs to be queried', required=True)
    sub_parser.set_defaults(func=task_query.task_query)


def btcaddress_query(subparsers: any) -> None:
    # Increase parameter calls for the Gen-Instance tasks query interface from user BTCAddress
    sub_parser = subparsers.add_parser('address_query', help='gen_instance tasks information query from BTCAddress')
    sub_parser.add_argument('--btcaddress', type=str, help='User BTC address required for query', required=True)
    sub_parser.set_defaults(func=address_query.address_query)


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
    cloud_workspace_group_create_cmd(subparsers=subparsers)
    cloud_workspace_group_list_cmd(subparsers=subparsers)
    cloud_product_list_cmd(subparsers=subparsers)

    # node -> cli
    node_new_account(subparsers=subparsers)
    node_register_node(subparsers=subparsers)

    # node_enroll_node(subparsers=subparsers)  #in installation script
    # node_disconnect_node(subparsers=subparsers)  #in uninstallation script

    node_query_all_nodes(subparsers=subparsers)
    node_query_node(subparsers=subparsers)
    node_query_node_incentive(subparsers=subparsers)

    # gen-instance
    geninstence_p2s(subparsers=subparsers)
    geninstence_taskQuery(subparsers=subparsers)
    btcaddress_query(subparsers=subparsers)

    # Parse the arguments
    args = parser.parse_args()
    # Check if 'func' attribute exists, then call it
    args.func(args) if hasattr(args, 'func') else parser.print_help()

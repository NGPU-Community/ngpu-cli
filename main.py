import argparse

from cli import version, cloud_image_create, cloud_image_list


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


if __name__ == '__main__':
    # create main parser
    parser = argparse.ArgumentParser(prog='NGPU', description='NGPU Cli')
    subparsers = parser.add_subparsers(help='NGPU Cli')

    # version cli
    version_cmd(subparsers=subparsers)

    # cloud-* cli
    cloud_image_create_cmd(subparsers=subparsers)
    cloud_image_list_cmd(subparsers=subparsers)

    # end
    args = parser.parse_args()
    args.func(args)

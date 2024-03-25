import argparse

from cli import version as ver


def version(parsers: any):
    # "version" command
    version_command = subparsers.add_parser('version', help='ngpu-cli version')
    # parser_image_create.add_argument('integers', metavar='N', type=int, nargs='+',
    #                                  help='an integer for the accumulator')
    version_command.set_defaults(func=ver.version())


def cloud_image_create():
    # TODO add child parser for the "sum" command
    parser_image_create = subparsers.add_parser('image-create', help='create docker image info, return image id')
    parser_image_create.add_argument('integers', metavar='N', type=int, nargs='+',
                                     help='an integer for the accumulator')
    parser_image_create.set_defaults(func=sum)


if __name__ == '__main__':
    # create main parser
    parser = argparse.ArgumentParser(description='Process some integers.')
    subparsers = parser.add_subparsers(help='sub-command help')

    version(subparsers)

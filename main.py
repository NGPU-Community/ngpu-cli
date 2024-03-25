import argparse

if __name__ == '__main__':
    # 创建一个主解析器
    parser = argparse.ArgumentParser(description='Process some integers.')
    subparsers = parser.add_subparsers(help='sub-command help')

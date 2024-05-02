import argparse
import logging
import os
from collections import namedtuple

logging.basicConfig(style='{',
                    filename='history.log',
                    level=logging.INFO,
                    filemode='a+',
                    encoding='utf8')
logger = logging.getLogger(__name__)

def get_file_paths(directory):
    return [os.path.join(root, filename) for root, _, files in os.walk(directory) for filename in files]

def inside_dir(path):
    logger.info(path)
    file_paths = get_file_paths(path)
    # logger.info(file_paths)
    data = []
    Content = namedtuple('Content', 'file_name ext flag_dir parent_dir', defaults=['', '', '', ''])
    for file_path in file_paths:
        *f,ext = file_path.split('.')
        if f:
            ext = f'.{ext}'
            *_, file = file_path.split('/')
            lenf = len(file)
            file_name = file[:-len(ext)]
            parent_path = str(file_path[:-lenf])
            flag_dir = ''
        else:
            *_, file_name = file_path.split('/')
            ext = ''
            lenf = len(file_name)
            parent_path = str(file_path[:-lenf])
            flag_dir = 'dir'
        data.append(Content(file_name, ext, flag_dir, parent_path))

    logger.info(data)
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Содержимое директории')
    parser.add_argument('param',
                        metavar='path',
                        type=str,
                        nargs=1,
                        help='enter path')
    args = parser.parse_args()
    print(inside_dir(*args.param))
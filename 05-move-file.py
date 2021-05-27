#!/usr/bin/env python3
# Usage: ./05-move-file.py
import os
from icecream import ic
import my_utils

source_dir = './data/'
destination_dir = source_dir+'processed/'


def main():
    filename = 'test.txt'

    # create test file
    my_utils.create_file(source_dir+filename)

    # use move function
    my_utils.move_file(source_dir+filename)

    # test if file has moved
    if os.path.isfile(destination_dir+filename):
        # delete test file
        my_utils.delete_file(destination_dir+filename)
        ic('test passed')
    else:
        ic()
        ic('test failed')

if __name__ == '__main__':
    main()

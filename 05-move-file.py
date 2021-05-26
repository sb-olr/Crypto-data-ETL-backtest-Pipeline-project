#!/usr/bin/env python3
# Usage: ./05-move-file.py
import os, shutil
from icecream import ic

source_dir = './data/'
destination_dir = source_dir+'processed/'


def delete_file(filename):
    os.remove(filename)
    ic('file delete done')

def move_file(filename, dest = destination_dir):
    shutil.move(filename, dest)
    ic('move file done')

def main():
    filename = 'test.txt'
    # create test file
    f = open(source_dir+filename, 'wt')
    f.close()

    # use move function
    move_file(source_dir+filename)

    # test if file has moved
    if os.path.isfile(destination_dir+filename):
        # delete test file
        delete_file(destination_dir+filename)
        ic('test passed')
    


if __name__ == '__main__':
    main()

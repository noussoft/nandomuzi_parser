#!/usr/bin/env python3

import os
import sys
import glob
import argparse

ROOT_DIR = '.'
OUTPUT_DIR = 'output'

def main():
    parser = setup_argparse()
    args = parser.parse_args()
    
    for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=False):
        if dir_name != '.':
            if args.verbose:
                print('Found directory: {}'.format(dir_name))
            for file in file_list:
                if 'small' in file:
                    os.remove(os.path.join(dir_name, file))
            os.chdir(dir_name)
            animated_file_name = os.path.join("..", dir_name + "_animated.gif")
            os.system("convert -delay 20 -loop 0 *jpg " + animated_file_name)
            if args.verbose:
                print('Animated gif was created: {}'.format(animated_file_name))
            os.chdir('..')
    make_thumbnails(OUTPUT_DIR, args.size)

def make_thumbnails(output_dir, size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file in glob.glob("*.gif"):
        os.system(
            "convert " + file + " -resize " + str(size) + "x" + str(size) + " "
            + os.path.join(OUTPUT_DIR, file)
        )
        os.remove(file)

def setup_argparse():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("size", type=int, help="size of thumbnail")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    return parser

if __name__ == '__main__':
    main()
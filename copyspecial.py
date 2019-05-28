#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "peter mayor"


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    '''returns a list of the absolute paths of the special files in dir'''
    output = [filename for filename in os.listdir(dir) if re.search(
        '__(.[A-Za-z]*)__', filename)]
    return output


def copy_to(paths, dir):
    '''given a list of paths, copies those files into the given directory'''
    for filename in paths:
        if os.path.isdir(dir):
            shutil.copy(filename, dir)
        else:
            os.mkdir(args.todir)
            shutil.copy(filename, dir)


def zip_to(zip_path):
    command = "compress-archive -literalpath %s -destinationpath %s.zip" \
        % (os.path.abspath('temp'), zip_path)
    print(command)
    subprocess.call([command])


def main():
    '''depending on arguments, copies or compresses or prints special files'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='source dir to copy from')
    args = parser.parse_args()

    special_paths = get_special_paths(args.from_dir)

    if not args.todir and not args.tozip:
        for filename in special_paths:
            print(filename)
    elif args.todir:
        copy_to(special_paths, args.todir)
    elif args.tozip:
        copy_to(special_paths, 'temp')
        zip_to(args.tozip)

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import sys
import os

def usage():
    if len(sys.argv) != 2:
        print("Usage: python3 ./tmp.py path_to_dir");
        sys.exit("Goodbye!!!");
    else:
        global path_to_dir, items;
        path_to_dir = sys.argv[1];
        items = os.listdir(path_to_dir);

def unify_format():
    for item in items:
        full_path_item = os.path.join(path_to_dir, item);
        if os.path.isfile(full_path_item):
            os.rename( full_path_item, full_path_item.replace("-", "_").replace("——", "_") );
        else:
            print("There has dir, exiting..");
            sys.exit(0);

def main():
    usage();
    unify_format();

main()

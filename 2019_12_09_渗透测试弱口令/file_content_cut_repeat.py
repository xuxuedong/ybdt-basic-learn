#!/usr/bin/python3

import sys

def usage():
    if len(sys.argv) != 2:
        print("Usage: python3 ./file_cut_repeat.py file_to_cut");
        sys.exit("Goodbye!!!");
    else:
        global file_name;
        file_name = sys.argv[1];

def file_cut_repeat():
    f = open(file_name, "r");
    lines = f.readlines();
    print(lines);
    tmp = [];
    for line in lines:
        if line not in tmp:
            tmp.append(line);
    f.close();

    f = open(file_name, "w");
    f.writelines(tmp);
    f.close();

def main():
    usage();
    file_cut_repeat();

main();

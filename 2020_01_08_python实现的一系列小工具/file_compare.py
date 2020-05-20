# coding=utf-8

import os
import os.path

array0 = os.listdir("御剑/御剑配置文件");
array1 = os.listdir("御剑后台扫描珍藏版/配置文件");

def cut_dir(a, partial_path):
    for each in a:
        a_cwd = os.path.join(os.getcwd(), partial_path);
        full_path = os.path.join(a_cwd, each);
        if os.path.isdir(full_path):
            a.remove(each);
    return a;

def main():
    var = "PHP.txt";
    a0 = open( os.path.join("御剑/御剑配置文件", var) );
    b0 = open( os.path.join("御剑后台扫描珍藏版/配置文件", var) );
    a0_content = a0.read();
    b0_content = b0.read();
    if a0_content == b0_content:
        print("yes, they are the same");
    else:
        print("no, they are different");

main();
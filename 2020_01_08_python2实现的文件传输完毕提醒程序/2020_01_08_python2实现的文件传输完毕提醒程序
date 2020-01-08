#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter.messagebox
import os

def main():
    while(True):
        str_obj = os.popen("tasklist");
        str_content = str_obj.read();
        if str_content.find("scp") != -1:
            break;
        else:
            continue;
    tkinter.messagebox.showinfo("提示", "文件传输完毕，给裕哥发送过去");

if __name__ == "__main__":
    main();

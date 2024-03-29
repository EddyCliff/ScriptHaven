'''
file: copy_files.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-03-29 15:48:57
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/copy_files.py
brief: 这个脚本的功能是实现文件夹A到文件夹B的文件复制。
       首先，脚本会检查文件夹A和文件夹B是否存在，如果不存在，则会输出错误信息并终止执行。
       然后，脚本会遍历文件夹A中的所有文件，并将它们复制到文件夹B。执行完成后，会输出“文件复制完成”。
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os
import shutil

def copy_files(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_folder, file)
            shutil.copy(src_file, dst_file)

def main():
    src_folder = input("请输入文件夹A的路径:")
    dst_folder = input("请输入文件夹B的路径:")

    if not os.path.exists(src_folder):
        print("文件夹A不存在, 请检查路径是否正确.")
        return

    if not os.path.exists(dst_folder):
        print("文件夹B不存在, 请检查路径是否正确.")
        return

    copy_files(src_folder, dst_folder)
    print("文件复制完成.")

if __name__ == "__main__":
    main()

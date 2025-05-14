'''
file: folder_and_file_lister_and_comparer.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-09-04 19:36:07
FilePath: /Eddy-hugo-papermodd:/git_repositories/ScriptHaven/Folder_handling_script/folder_and_file_lister_and_comparer.py
brief: 该代码文件的功能是列出指定路径下的第一层文件和文件夹名, 并将这些信息写入到txt文件中,
       然后比较两个txt文件的内容, 并将比较结果写入第三个txt文件中.
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os

def list_first_level_items(path):
    """列出指定路径下的第一层文件和文件夹名"""
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) or os.path.isfile(os.path.join(path, item))]

def write_to_txt(path, filename, content):
    """将内容写入指定路径下的txt文件"""
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
        for item in content:
            f.write(f"{item}\n")

def compare_txt_files(path1, path2, output_path):
    """比较两个txt文件的内容，并将结果写入第三个路径下的txt文件"""
    with open(path1, 'r', encoding='utf-8') as f1, open(path2, 'r', encoding='utf-8') as f2:
        content1 = set(f1.read().splitlines())
        content2 = set(f2.read().splitlines())

    diff = {
        "1.txt比2.txt多": content1 - content2,
        "2.txt比1.txt多": content2 - content1,
        "1.txt和2.txt的相同项": content1 & content2
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        for key, value in diff.items():
            f.write(f"{key} {len(value)}项\n")
            for item in value:
                f.write(f"{item}\n")

def main(path1, path2, path3):
    # 获取第一层文件和文件夹名
    items1 = list_first_level_items(path1)
    items2 = list_first_level_items(path2)

    # 写入txt文件
    write_to_txt(path1, '1.txt', items1)
    write_to_txt(path2, '2.txt', items2)

    # 比较txt文件内容
    compare_txt_files(os.path.join(path1, '1.txt'), os.path.join(path2, '2.txt'), os.path.join(path3, '3.txt'))

# 示例调用
path1 = r'E:\【剪辑师】灵感收藏\【剪辑师】灵感收集-音乐-人声为主-2024-09-05\B站-AI金冬天\合集_2024-06-29_AI COVER  Winter'
path2 = r'D:\Y_library\Y03_Video\合集_2024-09-05_AI COVER  Winter'
path3 = r'D:\Y_library\Y02_Picture'
main(path1, path2, path3)

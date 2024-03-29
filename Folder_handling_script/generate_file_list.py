'''
file: generate_file_list.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-03-21 07:49:12
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_7.py
brief: 该脚本会遍历某文件夹下的所有文件,将所有文件名按一行一个存储到list.txt中.
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''
import os

# 指定要扫描的文件夹路径
# folder_path = '/path/to/your/folder'  # 替换为实际扫描的文件夹路径
folder_path = 'D:/200_bywork/test'  # 替换为实际扫描的文件夹路径

output_file_path = os.path.join(folder_path, 'list.txt')  # 将输出文件保存在该文件夹下

# 确保目标文件夹存在，如果不存在则创建
os.makedirs(folder_path, exist_ok=True)

# 初始化行号计数器和过滤掉文本文件
line_number = 1
file_list = [f for f in sorted(os.listdir(folder_path)) if not f.endswith('.txt')]

# 打开或创建一个名为list.txt的文件以写入
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for filename in file_list:
        numbered_line = f"{line_number}) {filename}\n"
        output_file.write(numbered_line)
        line_number += 1

print("已完成文件名列表的生成，结果保存在", output_file_path, "中，已排除'.txt'文件。")

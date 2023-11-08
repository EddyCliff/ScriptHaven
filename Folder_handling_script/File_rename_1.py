'''
file: File_rename_1.py
author: EddyCliff
date: Do not edit
LastEditTime: 2023-11-08 13:57:54
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_1.py
brief: 这个 Python 脚本用于重命名指定文件夹中的所有文件。
*      它会遍历指定文件夹内的所有文件，检查文件名中是否包含空格，并将空格替换为下划线。
*      重命名后的文件将保留在原文件夹内，旧文件名和新文件名都将打印出来以供确认。
copyright (c) 2023 by EddyCliff, All Rights Reserved. 
'''

import os

# 设置要操作的文件夹路径

folder_path = "D:/iiii"

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查是否为文件
    if os.path.isfile(os.path.join(folder_path, filename)):
        # 删除文件名中的空格，并组成新的文件名
        new_filename = filename.replace(" ", "")
        
        # 重命名文件
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"重命名文件: {filename} -> {new_filename}")

print("完成重命名操作。")

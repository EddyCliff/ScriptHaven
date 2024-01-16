'''
file: 
author: EddyCliff
date: Do not edit
LastEditTime: 2024-01-16 19:04:13
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_5.py
brief: 该脚本会遍历某文件夹下的所有文件,将所有文件名重命名加上.jpg,意思就是文件名本来是1,那么执行脚本后将变为1.jpg.
*      同理,你也可以一次性添加其他后缀.
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os

folder_path = "D:/your_folder"  # 替换为你的文件夹路径

# 遍历文件夹中的所有文件
file_list = os.listdir(folder_path)

# 遍历文件夹中的所有文件，重命名文件
for filename in file_list:
    # 检查是否为文件
    if os.path.isfile(os.path.join(folder_path, filename)):
        # 构建新的文件名，加上 ".jpg" 扩展名
        new_filename = f"{filename}.jpg"

        # 重命名文件
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"重命名文件: {filename} -> {new_filename}")

print("完成重命名操作。")

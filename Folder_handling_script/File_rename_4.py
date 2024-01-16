'''
file: 
author: EddyCliff
date: Do not edit
LastEditTime: 2024-01-16 19:51:44
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_4.py
brief: 该脚本可以遍历指定文件夹下的所有文件,实现按数字依次命名,而之前文件名本身就是数字的文件将不作改变.
*      同时,重命名过程中保持文件格式前后不变.
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os

folder_path = "D:/your_folder" #设置文件夹路径

# 遍历文件夹中的所有文件
file_list = os.listdir(folder_path)

# 用于存储已经命名的数字
numbered_files = set()

# 提取已经命名的数字文件
for filename in file_list:
    try:
        numbered_files.add(int(filename.split('.')[0]))
    except ValueError:
        pass

# 遍历文件夹中的所有文件，重命名非数字文件
for filename in file_list:
    # 检查是否为文件
    if os.path.isfile(os.path.join(folder_path, filename)):
        # 检查是否为数字文件，如果是，则跳过
        try:
            int(filename.split('.')[0])
            continue
        except ValueError:
            pass

        # 找到下一个可用的数字命名
        new_number = 1
        while new_number in numbered_files:
            new_number += 1

        # 获取文件扩展名
        file_extension = filename.split('.')[-1]

        # 构建新的文件名，保证格式为jpg
        new_filename = f"{new_number}.{file_extension}"

        # 重命名文件
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"重命名文件: {filename} -> {new_filename}")
        numbered_files.add(new_number)

print("完成重命名操作。")

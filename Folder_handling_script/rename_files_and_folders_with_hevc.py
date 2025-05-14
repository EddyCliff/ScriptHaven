'''
file: rename_files_and_folders_with_hevc.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-09-04 21:28:43
FilePath: /Eddy-hugo-papermodd:/git_repositories/ScriptHaven/Folder_handling_script/rename_files_and_folders_with_hevc.py
brief: 遍历指定目录中的所有文件和文件夹，
       并在它们的名称后面添加“-[HEVC编码]”字符串，以实现批量重命名的目的。
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os

def rename_files_and_folders_in_directory(directory_path):
    # 确保路径存在
    if not os.path.exists(directory_path):
        print(f"路径 {directory_path} 不存在！")
        return
    
    # 遍历目录
    files = os.listdir(directory_path)
    count = 0
    
    for file in files:
        # 构建完整的文件路径
        src = os.path.join(directory_path, file)
        
        # 分离文件名和扩展名
        filename, extension = os.path.splitext(file)
        
        # 新的文件名/文件夹名
        new_name = f"{filename}-[HEVC编码]" + (extension if extension else '')
        
        # 构建新的文件路径
        dst = os.path.join(directory_path, new_name)
        
        # 检查是否已经存在同名文件/文件夹，避免覆盖
        if os.path.exists(dst):
            print(f"警告：文件/文件夹 {dst} 已经存在，跳过重命名 {file}")
            continue
        
        # 重命名文件或文件夹
        os.rename(src, dst)
        count += 1
    
    print(f"已更改完成，共更改了{count}个文件/文件夹")

# 使用方法
directory_path = r'D:\Y_library\Y03_Video\合集_2024-09-04_女团'
rename_files_and_folders_in_directory(directory_path)
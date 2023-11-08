'''
file: File_rename_3.py
author: EddyCliff
date: Do not edit
LastEditTime: 2023-11-08 14:02:16
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_3.py
brief: 该脚本是为了重命名指定文件夹下所有以“.mp4”结尾的文件名,并且删除文件名中的"教程."。
copyright (c) 2023 by EddyCliff, All Rights Reserved. 
'''
import os  
  
# 设置要操作的文件夹路径  
folder_path = "D:/edge download/qianfeng/kecheng/10"  
  
# 遍历文件夹中的所有文件  
for filename in os.listdir(folder_path):  
    # 检查是否为文件  
    if os.path.isfile(os.path.join(folder_path, filename)):  
        # 检查文件名是否以 ".mp4" 结尾  
        if filename.endswith(".mp4"):  
            # 删除文件名中的指定字符串  
            new_filename = filename.replace("教程.", "")  
            # 重命名文件  
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))  
            print(f"重命名文件: {filename} -> {new_filename}")  
  
print("完成重命名操作。")
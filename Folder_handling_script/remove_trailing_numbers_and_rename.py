'''
file: remove_trailing_numbers_and_rename.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-09-07 18:55:42
FilePath: /Eddy-hugo-papermodd:/git_repositories/ScriptHaven/Folder_handling_script/remove_trailing_numbers_and_rename.py
brief: 该脚本用于遍历指定目录中的所有文件和文件夹，通过正则表达式匹配文件名中形如-123456789的末尾数字序列，
       并将其移除，确保新文件名在目录中唯一，最后重命名文件并输出更改的数量。
       使用时记得更改指定路径.
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os
import re

def rename_files_in_directory(path):
    # 检查路径是否存在
    if not os.path.exists(path):
        print(f"路径 {path} 不存在！")
        return
    
    # 初始化计数器
    count = 0
    
    # 定义正则表达式模式
    pattern = r'-\d+$'  # 匹配形如-123456789的形式，位于字符串末尾
    
    # 存储已经更改过的文件名
    renamed_files = {}
    
    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(path):
        # 构建完整的文件路径
        full_path = os.path.join(path, filename)
        
        # 使用正则表达式匹配
        match = re.search(pattern, filename)
        
        # 如果找到了匹配项
        if match:
            base_name = re.sub(pattern, '', filename)
            
            # 确保新文件名唯一
            new_filename = base_name
            counter = 1
            
            while new_filename in renamed_files.values() or os.path.exists(os.path.join(path, new_filename)):
                new_filename = f"{base_name}-({counter})"
                counter += 1
            
            # 更新新的完整路径
            new_full_path = os.path.join(path, new_filename)
            
            # 重命名文件
            os.rename(full_path, new_full_path)
            
            # 更新已更改文件名的记录
            renamed_files[filename] = new_filename
            
            # 计数器加一
            count += 1
    
    # 打印完成信息
    print(f"已更改完成，共更改了 {count} 个文件(文件夹)")

# 指定路径
directory_path = r'D:\Y_library\Y03_Video\分集_2024-09-07_了解社会如何影响个体，训练逻辑思考及表达能力——社会心理学 NTHU 陈舜文'

# 调用函数，传入指定路径
rename_files_in_directory(directory_path)
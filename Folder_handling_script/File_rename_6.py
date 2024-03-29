'''
file: File_rename_6.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-02-03 14:04:26
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_6.py
brief: 该脚本会遍历某文件夹下的所有文件,对文件进行重命名.
*      比如《下午736 · 2023年11月29日》,那么运行脚本之后文件名应该变为《2023年11月29日-下午736》.
*      比如《下午736 · 2023年11月29日(1)》,那么运行脚本之后文件名应该变为《2023年11月29日-下午736(1)》,中英文括号都能识别.
*      运行脚本之后文件格式前后不发生改变.
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os
import re

def rename_files_in_folder(folder_path):
    # 遍历文件夹下的所有文件
    for filename in os.listdir(folder_path):
        # 检查是否为文件（而不是子目录）
        if os.path.isfile(os.path.join(folder_path, filename)):
            # 分离出文件名和扩展名
            base_name, ext = os.path.splitext(filename)
            
            # 处理包含特殊格式的文件名
            parts = base_name.split(' · ')
            if len(parts) == 2:
                # 将时间部分与日期部分交换并添加括号中的序号（无论中英文括号）
                time_part, date_part = parts
                sequence_number = ""
                
                # 使用正则表达式查找最后一个左括号(中文或英文)和对应的右括号
                match = re.search(r'([\(\[]).*?([\)\]])', date_part)
                if match:
                    left_bracket, right_bracket = match.groups()
                    sequence = date_part[match.start():match.end()]
                    date_part = date_part[:match.start()]
                    sequence_number = f"{left_bracket}{sequence}{right_bracket}"

                new_base_name = f"{date_part} - {time_part}{sequence_number}"
                new_filename = f"{new_base_name}{ext}"

                # 构建旧文件路径和新文件路径
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, new_filename)

                # 执行重命名操作，并给出反馈
                try:
                    os.rename(old_file, new_file)
                    print(f"成功重命名文件: {old_file} -> {new_file}")
                except Exception as e:
                    print(f"未能重命名文件 {old_file} 到 {new_file}：{e}")
            else:
                print(f"跳过文件 {filename} - 文件名不符合预期格式")

# 使用函数，提供要处理的文件夹路径
folder_to_process = r"D:\Y_library\Y01_Software\download\test"
rename_files_in_folder(folder_to_process)
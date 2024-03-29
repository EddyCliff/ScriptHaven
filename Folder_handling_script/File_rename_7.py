'''
file: File_rename_7.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-03-29 16:01:47
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_7.py
brief: 该脚本的主要功能是对指定文件夹内的所有文件进行重命名。
*      用户需要输入文件夹的路径和新的命名规则，脚本会自动为文件夹内的每个文件添加新的命名。
*      例如，如果文件夹内有名为"1.jpg"的文件，新的命名规则为"[PIC]"，那么该文件将被重命名为"[PIC]_1.jpg"。
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os

def rename_files(folder_path, naming_rule):
    try:
        # 获取文件夹下的所有文件
        files = os.listdir(folder_path)

        # 初始化文件计数器
        file_counter = 1

        for file in files:
            # 检查是否为文件
            if os.path.isfile(os.path.join(folder_path, file)):
                # 获取文件名和扩展名
                file_name, file_extension = os.path.splitext(file)

                # 构建新文件名
                new_file_name = f"[{naming_rule}]_{file_counter}{file_extension}"

                # 重命名文件
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file_name))

                # 更新文件计数器
                file_counter += 1

        # 打印成功信息
        print("文件重命名成功！")

    except Exception as e:
        # 打印失败信息和错误原因
        print(f"文件重命名失败！错误原因：{e}")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径和命名规则
    folder_path = input("请输入指定文件夹路径：")
    naming_rule = input("请输入命名规则：")

    # 调用函数重命名文件
    rename_files(folder_path, naming_rule)
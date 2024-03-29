'''
file: File_rename_8.py
author: EddyCliff
date: Do not edit
LastEditTime: 2024-03-29 15:55:02
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/File_rename_9.py
brief: 该Python脚本的主要功能是对指定文件夹内的所有文件进行重命名。
*      用户需要输入文件夹的路径和新的命名规则，脚本会自动为文件夹内的每个文件添加新的命名。
*      例如，如果文件夹内有名为"1.jpg"的文件，新的命名规则为"[PIC]"，那么该文件将被重命名为"[PIC]_1.jpg"。
*      该脚本首先会验证用户输入的文件夹路径是否有效，如果无效则会输出错误信息并终止执行。
*      然后，脚本会遍历文件夹内的所有文件，并对每个文件进行重命名。
*      如果重命名过程中出现文件名冲突或重命名失败的情况，脚本会输出错误信息并跳出循环。
*      如果所有文件的重命名都成功，脚本会输出成功信息。
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os
import logging

# 设置日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_folder_path(folder_path):
    """
    验证文件夹路径的有效性。
    """
    if not os.path.isdir(folder_path):
        logging.error("输入的路径不是一个有效的文件夹。")
        raise ValueError("输入的路径不是一个有效的文件夹。")

def rename_file(file_path, file_counter, naming_rule):
    """
    重命名单个文件。
    """
    file_name, file_extension = os.path.splitext(file_path)
    new_file_name = f"[{naming_rule}]_{file_counter}{file_extension}"
    if os.path.exists(os.path.join(folder_path, new_file_name)):
        logging.error(f"文件名冲突：{new_file_name}")
        return False
    try:
        os.rename(file_path, os.path.join(folder_path, new_file_name))
        return True
    except Exception as e:
        logging.error(f"重命名文件失败：{e}")
        return False

def rename_files(folder_path, naming_rule):
    try:
        validate_folder_path(folder_path)

        # 获取文件夹下的所有文件
        files = os.listdir(folder_path)

        # 初始化文件计数器
        file_counter = 1

        for file in files:
            full_file_path = os.path.join(folder_path, file)
            # 检查是否为文件
            if os.path.isfile(full_file_path):
                if rename_file(full_file_path, file_counter, naming_rule):
                    file_counter += 1
                else:
                    # 如果文件重命名失败，则跳出循环
                    break

        # 打印成功信息
        logging.info("文件重命名成功！")

    except ValueError as ve:
        logging.error(f"输入错误：{ve}")
    except Exception as e:
        logging.error(f"文件重命名失败！错误原因：{e}")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径和命名规则
    folder_path = input("请输入指定文件夹路径：")
    naming_rule = input("请输入命名规则：")

    # 调用函数重命名文件
    rename_files(folder_path, naming_rule)
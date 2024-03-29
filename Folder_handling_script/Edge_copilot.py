'''
file: 
author: EddyCliff
date: Do not edit
LastEditTime: 2024-03-29 15:46:57
FilePath: /知乎MarKdownd:/git_repositories/ScriptHaven/Folder_handling_script/Edge_copilot.py
brief: 打开Edge的Copilot权限
copyright (c) 2024 by EddyCliff, All Rights Reserved. 
'''

import os
import json

user_data_path = os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data')  # 指定浏览器用户数据目录的路径

if not os.path.exists(user_data_path):
    print('未找到文件', user_data_path)
    exit()

for file in os.listdir(user_data_path):
    if file != 'Default' and not file.startswith('Profile '):
        continue
    preferences_path = os.path.join(user_data_path, file, 'Preferences')
    with open(preferences_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)

    if json_data['browser'].get('chat_ip_eligibility_status') in [None, False]:
        json_data['browser']['chat_ip_eligibility_status'] = True
        with open(preferences_path, 'w', encoding='utf-8') as fp:
            json.dump(json_data, fp)
        print('成功修改', file, '的Preferences文件')
    else:
        print(file, '没有需要修改的地方')

input('按Enter退出...')
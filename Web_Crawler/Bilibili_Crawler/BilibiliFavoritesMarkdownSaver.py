import os
import requests
from bilibili_api import bilibili

# 从终端获取保存路径和会话信息
save_path = input("请输入Markdown文件的保存路径：")
session_info = {
    'sessdata': input("请输入您的SESSDATA: "),
    'bili_jct': input("请输入您的bili_jct: "),
    'buvid3': input("请输入您的buvid3: "),
    'dedeuserid': input("请输入您的DedeUserID: "),
    'ac_time': input("请输入您的ac_time_value: "),
}

# 确保保存路径的目录存在
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 使用bilibili-api-python库获取个人收藏夹信息
def fetch_favorites(session_info, save_path):
    bilibili = bilibili(session_info)
    favorites = bilibili.favorites('video', pages=10)  # pages参数表示请求的页数
    
    # 构建Markdown文件名
    filename = 'favorites.md'
    markdown_file_path = os.path.join(save_path, filename)
    
    # 将收藏夹视频信息保存为Markdown文件
    with open(markdown_file_path, 'w', encoding='utf-8') as f:
        for favorite in favorites:
            title = favorite['title']
            aid = favorite['aid']
            url = f'https://www.bilibili.com/video/av{aid}'
            f.write(f'- [{title}]({url})\n')
    
    return markdown_file_path

# 主函数
def main():
    markdown_file_path = fetch_favorites(session_info, save_path)
    if markdown_file_path:
        print(f'收藏夹视频信息已成功保存到Markdown文件：{markdown_file_path}')
    else:
        print('获取收藏夹视频信息失败。')

if __name__ == '__main__':
    main()
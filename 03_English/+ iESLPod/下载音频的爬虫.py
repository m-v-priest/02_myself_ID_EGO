'''
我有一些音频要下载, 地址规律如下:

http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/0001_iESLPod.com.mp3
http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/0002_iESLPod.com.mp3
...
http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/0099_iESLPod.com.mp3
http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/0100_iESLPod.com.mp3

请用python编写一个爬虫程序, 能单线程的, 一个个依次下载这些音频文件.

注意: 为了避免被网站封杀爬虫, 请你每下完一个音频文件后, 随机停顿一个1到2秒间的随机毫秒数.
'''


import requests
import time
import random


def download_ieslpod_audios():
    base_url = "http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    for episode in range(4, 101):
        # 生成四位数的编号字符串
        episode_str = f"{episode:04d}"
        filename = f"{episode_str}_iESLPod.com.mp3"
        file_url = base_url + filename

        try:
            # 发送HTTP请求
            response = requests.get(file_url, headers=headers, timeout=10)
            response.raise_for_status()

            # 保存文件
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"成功下载第 {episode_str} 个文件")

        except Exception as e:
            print(f"下载 {filename} 失败，错误信息: {str(e)}")

        # 随机延迟（1-2秒之间）
        delay = random.uniform(1, 2)
        time.sleep(delay)


if __name__ == "__main__":
    download_ieslpod_audios()
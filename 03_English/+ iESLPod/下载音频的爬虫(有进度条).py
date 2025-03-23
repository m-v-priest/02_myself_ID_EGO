
'''

http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/0006_iESLPod.com.mp3
http://www.ieslpod.com/media/01_Daily_English/Daily_English_0001_0100/0100_iESLPod.com.mp3
http://www.ieslpod.com/media/01_Daily_English/Daily_English_0101_0200/0101_iESLPod.com.mp3

http://www.ieslpod.com/media/01_Daily_English/Daily_English_0701_0800/0701_iESLPod.com.mp3

http://www.ieslpod.com/media/01_Daily_English/Daily_English_0901_1000/0901_iESLPod.com.mp3
http://www.ieslpod.com/media/01_Daily_English/Daily_English_1201_1305/1305_iESLPod.com.mp3





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
    base_url = "http://www.ieslpod.com/media/01_Daily_English/Daily_English_1001_1101/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    for episode in range(1001, 1101):
        episode_str = f"{episode:04d}"
        filename = f"{episode_str}_iESLPod.com.mp3"
        file_url = base_url + filename

        try:
            # 启用流式下载
            with requests.get(file_url, headers=headers, stream=True, timeout=20) as response:
                response.raise_for_status()

                # 获取文件总大小（字节）
                total_size = int(response.headers.get('Content-Length', 0))
                downloaded = 0

                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)

                            # 生成进度条
                            if total_size > 0:
                                percent = downloaded / total_size * 100
                                bars = "|" * int(percent // 10)  # 每10%一个竖线
                                print(f"\r下载进度 [{bars.ljust(10)}] {percent:.1f}%", end='')

                # 下载完成换行
                print(f"\n✅ 成功下载 {filename}")

        except Exception as e:
            print(f"\n❌ 下载失败 {filename}: {str(e)}")

        # 随机延迟（1-2秒）
        time.sleep(random.uniform(1, 2))


if __name__ == "__main__":
    download_ieslpod_audios()
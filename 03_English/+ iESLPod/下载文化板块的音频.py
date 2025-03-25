
'''

我有一批音频 (共603个音频文件)要下载, 它们的地址规律如下:
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_001_060/001_iESLPod.com.mp3
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_001_060/002_iESLPod.com.mp3
...
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_001_060/059_iESLPod.com.mp3
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_001_060/060_iESLPod.com.mp3

http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_061_120/061_iESLPod.com.mp3
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_061_120/062_iESLPod.com.mp3
...
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_061_120/120_iESLPod.com.mp3

...

http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_541_603/541_iESLPod.com.mp3
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_541_603/542_iESLPod.com.mp3
...
http://www.ieslpod.com/media/02_Cultural_English/Cultural_English_541_603/603_iESLPod.com.mp3


即规律是, 大体上每隔60个音频文件, 链接地址中的"Cultural_English_001_060"中的数字会变化.
如, 第1到60个音频文件, 链接地址中的"Cultural_English_001_060"中的数字是 001到060.
第61-120个音频文件, 链接地址中的"Cultural_English_061_120"中的数字是 061到120.
...
最后一批和前面的不同, 前面的每批都只有60个音频, 而最后一批有63个音频, 所以第541-603个音频文件, 链接地址中的"Cultural_English_541_603"中的数字是 541到603.

请用python编写一个爬虫程序, 能单线程的, 一个个依次下载这些音频文件. 同时, 在下载每个文件的过程中, 要给出这个文件当前的进度, 即下载百分比数值.

注意: 为了避免被网站封杀爬虫, 请你每下完一个音频文件后, 随机停顿一个1到2秒间的随机毫秒数.

另外, 不用输出推理过程, 直接给出结果就行.

'''

import requests
import time
import random
import os


def download_ieslpod_audios():
    save_dir = 'ieslpod_audios'
    os.makedirs(save_dir, exist_ok=True)

    directory_groups = [
        (1, 60), (61, 120), (121, 180), (181, 240), (241, 300),
        (301, 360), (361, 420), (421, 480), (481, 540), (541, 603)
    ]

    total_files = 0
    for group_start, group_end in directory_groups:
        dir_part = f"Cultural_English_{group_start:03d}_{group_end:03d}"

        for file_num in range(group_start, group_end + 1):
            url = f"http://www.ieslpod.com/media/02_Cultural_English/{dir_part}/{file_num:03d}_iESLPod.com.mp3"
            filename = os.path.join(save_dir, f"{file_num:03d}.mp3")

            print(f"[{file_num:03d}] 开始下载...", end='', flush=True)
            try:
                with requests.get(url, stream=True, timeout=30) as response:
                    response.raise_for_status()

                    # 获取文件总大小
                    total_size = int(response.headers.get('content-length', 0))
                    downloaded = 0

                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:  # 过滤空白块
                                f.write(chunk)
                                downloaded += len(chunk)

                                # 计算并显示进度
                                if total_size > 0:
                                    progress = downloaded / total_size * 100
                                    print(f"\r[{file_num:03d}] 下载中... {progress:.1f}%", end='', flush=True)

                    # 下载完成提示
                    file_size = downloaded / (1024 * 1024)  # 转换为MB
                    print(f"\r[{file_num:03d}] 下载完成! {file_size:.1f}MB    ")
                    total_files += 1

            except Exception as e:
                print(f"\r[{file_num:03d}] 下载失败! {str(e)}      ")

            # 随机延迟（1-2秒）
            time.sleep(random.uniform(1, 2))

    print(f"\n全部下载完成！共成功下载 {total_files} 个文件")


if __name__ == "__main__":
    download_ieslpod_audios()
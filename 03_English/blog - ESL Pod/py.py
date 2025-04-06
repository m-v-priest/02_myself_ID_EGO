
'''
在下面的网站上, 有很多英语文章.
规律为:
http://www.ieslpod.com/?list_2/6.html   这个地址上, 是有编号为0006 的文章.
http://www.ieslpod.com/?list_2/7.html   这个地址上, 是有编号为0007 的文章.
...
http://www.ieslpod.com/?list_2/50.html   这个地址上, 是有编号为0050 的文章.

所有这些页面中的文章, 都包裹在这个html标签中: <div class="content mb-3"> ... </div>, 即 class类名为"content mb-3" 的 div标签里.

请你用python代码, 编写一个爬虫程序, 能帮我把这50个页面中的英语文章批量下载下来, 提取出里面的纯文本内容, 不要带有html标签, 但是要保留换行! 即, 遇到<br>换行标签时, 要把它用两个换行符 \r\n\r\n 来代替.并且分别存入名字叫 "0006.adoc", "0007.adoc", ... "0050.adoc" 的扩展名是 adoc 的文件中.

注意: 爬虫程序在爬取每一个页面后, 必须保留1秒钟的中间停顿时间, 以免被网站封杀.


'''

import requests
from bs4 import BeautifulSoup
import time
import os

os.makedirs('articles', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def process_br_tags(element):
    """递归处理所有标签，特别处理<br>标签"""
    text = ''
    for elem in element.contents:
        if isinstance(elem, str):
            text += elem.strip()
        elif elem.str人才名字 == 'br':
            text += '\r\n\r\n'  # 双换行符
        else:
            text += process_br_tags(elem)
    return text


def extract_content(html):
    """提取内容并保留换行格式"""
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='content mb-3')

    if not content_div:
        return None

    # 处理特殊换行
    formatted_text = process_br_tags(content_div)

    # 清理多余空白但保留换行
    return '\n'.join([line.strip() for line in formatted_text.split('\n') if line.strip()])


def save_article(content, filename):
    """保存到adoc文件"""
    path = os.path.join('articles', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已保存: {filename}")


def crawl_articles():
    """主爬虫函数"""
    for n in range(100, 101):
        article_id = f"{n:04d}"
        url = f"http://www.ieslpod.com/?list_2/{n}.html"
        filename = f"{article_id}.adoc"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            content = extract_content(response.text)
            if content:
                save_article(content, filename)
            else:
                print(f"内容为空: {filename}")

        except requests.exceptions.RequestException as e:
            print(f"请求失败 {filename}: {str(e)}")
        except Exception as e:
            print(f"处理错误 {filename}: {str(e)}")

        time.sleep(1)


if __name__ == "__main__":
    crawl_articles()
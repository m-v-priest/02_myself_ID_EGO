



import requests
from bs4 import BeautifulSoup
import time
import os

os.makedirs('articles', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def generate_metadata(article_id):
    """生成AsciiDoc元数据头"""
    return f"""= {article_id}
:toc: left
:toclevels: 3
:sectnums:
:stylesheet: ../../../myAdocCss.css

'''

== 
"""


def process_br_tags(element):
    """处理换行标签"""
    text = ''
    for elem in element.contents:
        if isinstance(elem, str):
            text += elem.strip()
        elif elem.name == 'br':
            text += '\r\n\r\n'
        else:
            text += process_br_tags(elem)
    return text


def extract_content(html):
    """提取文章内容"""
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='content mb-3')

    if not content_div:
        return None

    formatted_text = process_br_tags(content_div)
    return '\n'.join([line.strip() for line in formatted_text.split('\n') if line.strip()])


def save_article(content, article_id):
    """保存文件并添加元数据头"""
    filename = f"{article_id}.adoc"
    metadata = generate_metadata(article_id)
    full_content = f"{metadata}\n{content}"

    path = os.path.join('articles', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    print(f"已保存: {filename}")


def crawl_articles():
    """主爬虫函数"""
    for n in range(1846, 1909):
        article_id = f"{n:04d}"
        url = f"http://www.ieslpod.com/?list_25/{n}.html"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            content = extract_content(response.text)
            if content:
                save_article(content, article_id)
            else:
                print(f"内容为空: {article_id}")

        except requests.exceptions.RequestException as e:
            print(f"请求失败 {article_id}: {str(e)}")
        except Exception as e:
            print(f"处理错误 {article_id}: {str(e)}")

        time.sleep(1)


if __name__ == "__main__":
    crawl_articles()
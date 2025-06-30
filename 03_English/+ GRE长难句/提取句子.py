

'''
我有一个html网页, 在我win10电脑的桌面上, 文件名叫 all.html


该html文件里面有很多的英文句子, 每个句子都被包裹在 <p class="kindle-cn-para-no-indent"> 和 </p> 中间.

比如:
<p class="kindle-cn-para-no-indent">We are hard pressed on every side, but not crushed; perplexed, but not in despair; persecuted, but not abandoned; struck down, but not destroyed.</p>

请你给出python程序代码, 能提取出这个html文件中的所有上面被包裹的英文句子.

最终输出的格式要求为:

- 英文句子1

- 英文句子2

- 英文句子3

...

即每个句子用markdown中的列表来表示



'''


from bs4 import BeautifulSoup
import os

def extract_sentences_from_html(file_path):
    # 读取HTML文件
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找所有指定class的p标签
    p_tags = soup.find_all('p', class_='kindle-cn-para-no-indent')

    # 提取文本内容并去除首尾空白
    sentences = [p.get_text(strip=True) for p in p_tags]

    # 以Markdown列表格式输出
    for sentence in sentences:
        print(f"- {sentence}")

# 指定文件路径（请替换为你的实际路径）
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
html_file_path = os.path.join(desktop_path, 'all.html')

# 调用函数
extract_sentences_from_html(html_file_path)
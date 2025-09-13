import re
import os
from bs4 import BeautifulSoup, Tag, NavigableString
from tqdm import tqdm


def count_words(input_file):
    """统计文件中的单词数量（通过统计'あ'的数量）"""
    word_count = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if 'あ' in line:
                word_count += 1
    return word_count


def extract_text(soup):
    """智能提取文本内容，添加分割线并优化格式"""
    output = []
    last_text = ""
    last_element = None

    def process_element(element):
        nonlocal last_text, last_element

        if isinstance(element, Tag):
            # 处理音标部分 - 合并为一行
            if element.name in ['pron-g', 'phon-blk', 'phon']:
                text = element.get_text(strip=True, separator=" ")
                if text and text != last_text:
                    # 添加空格避免粘连
                    if output and not output[-1].endswith((' ', '\n')):
                        output.append(" ")
                    output.append(text)
                    last_text = text
                    last_element = element
                return

            # 处理例句标签 - 单独一行
            if element.name == 'x':
                text = element.get_text(" ", strip=True)
                if text and text != last_text:
                    output.append("\n◆ " + text)
                    last_text = text
                    last_element = element
                return

            # 处理释义标题 - 添加两个换行和分割线
            if '➤' in element.get_text():
                text = element.get_text(" ", strip=True)
                if text and text != last_text:
                    # 添加分割线
                    if last_element and last_element.name != 'h':
                        output.append("\n" + "=" * 50 + "\n")
                    output.append(text)
                    last_text = text
                    last_element = element
                return

            # 处理语法标签 - 添加分割线
            if element.name in ['gram', 'reg', 'geo']:
                text = element.get_text(" ", strip=True)
                if text and text != last_text:
                    # 添加分割线
                    if last_element and last_element.name != 'gram':
                        output.append("\n" + "-" * 40 + "\n")
                    output.append(text)
                    last_text = text
                    last_element = element
                return

            # 处理其他关键标签
            if element.name in ['h', 'def', 'sn-g', 'idm', 'pv']:
                text = element.get_text(" ", strip=True)
                if text and text != last_text:
                    output.append(text)
                    last_text = text
                    last_element = element
                return

            # 递归处理子元素
            for child in element.children:
                process_element(child)

        elif isinstance(element, NavigableString):
            text = element.strip()
            if text and text != last_text:
                # 添加空格避免粘连
                if output and not output[-1].endswith((' ', '\n')):
                    output.append(" ")
                output.append(text)
                last_text = text
                last_element = element

    # 开始处理DOM
    for child in soup.children:
        process_element(child)

    return "".join(output)


def clean_text(text):
    """清理文本，优化格式"""
    # 确保每个◆在单独一行
    text = re.sub(r'◆', '\n◆', text)

    # 确保每个➤前有分割线
    text = re.sub(r'➤', '\n' + '=' * 50 + '\n➤', text)

    # 确保语法标签前有分割线
    text = re.sub(r'(\[.*?\])', '\n' + '-' * 40 + '\n\\1', text)

    # 压缩多余的空格
    text = re.sub(r'[ \t]{2,}', ' ', text)

    # 压缩多余的空行
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 移除行首行尾多余空格
    text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)

    return text


def process_chunk(chunk):
    """处理单个单词块"""
    soup = BeautifulSoup(chunk, 'html.parser')
    text = extract_text(soup)
    text = clean_text(text)
    return text


def main():
    input_file = "提纯 牛津高阶英汉双解词典（第9版）.txt"
    output_file = "extracted_pure_all.txt"

    # 统计单词数量
    total_words = count_words(input_file)
    print(f"文件中共有 {total_words} 个单词")

    # 创建进度条
    progress_bar = tqdm(total=total_words, desc="处理单词", unit="word")

    # 读取输入文件并处理
    with open(input_file, 'r', encoding='utf-8') as f_in, \
            open(output_file, 'w', encoding='utf-8') as f_out:

        current_chunk = []
        word_count = 0

        for line in f_in:
            # 检测到新单词开始
            if 'あ' in line:
                # 处理当前单词块
                if current_chunk:
                    chunk_text = ''.join(current_chunk)
                    processed_text = process_chunk(chunk_text)
                    f_out.write(processed_text + '\n\n')

                    # 更新进度条
                    word_count += 1
                    progress_bar.update(1)

                # 开始新单词块
                current_chunk = [line]
            else:
                # 继续当前单词块
                current_chunk.append(line)

        # 处理最后一个单词块
        if current_chunk:
            chunk_text = ''.join(current_chunk)
            processed_text = process_chunk(chunk_text)
            f_out.write(processed_text + '\n\n')
            word_count += 1
            progress_bar.update(1)

    # 关闭进度条
    progress_bar.close()
    print(f"处理完成！共处理 {word_count} 个单词")


if __name__ == '__main__':
    main()
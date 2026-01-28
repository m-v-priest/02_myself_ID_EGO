import os
import re
import requests
from bs4 import BeautifulSoup, NavigableString


def is_gray_box(element):
    """判断是否为灰色背景块 (Learning Objectives, Milestone 等)"""
    if isinstance(element, NavigableString):
        return False
    classes = element.get('class', [])
    data_type = element.get('data-type', '')
    # 扩大识别范围，确保抓取到所有灰色块
    gray_patterns = ['os-note', 'abstract', 'note', 'box', 'sidebar', 'learning-objectives']
    if any(p in classes for p in gray_patterns) or data_type in gray_patterns:
        return True
    return False


def html_to_adoc(element, in_gray_box=False):
    """递归转换 HTML 到 Asciidoc，遵守符号和公式规范"""
    if isinstance(element, NavigableString):
        # 严格遵守：直接输出箭头符号
        text = str(element).replace("->", "→").replace("<-", "←")
        text = text.replace("=>", "→").replace("<=", "←")
        return text

    # 处理灰色块模板
    if not in_gray_box and is_gray_box(element):
        content = ""
        for child in element.children:
            content += html_to_adoc(child, in_gray_box=True)
        return f"\n[.my1]\n.案例\n====\n{content.strip()}\n====\n\n"

    result = ""
    # 标题处理
    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(element.name[1])
        result += f"\n{'=' * level} {element.get_text().strip()}\n\n"
    elif element.name == 'p':
        content = "".join(html_to_adoc(child, in_gray_box) for child in element.children)
        result += f"{content.strip()}\n\n"
    # 列表处理
    elif element.name in ['ul', 'ol']:
        symbol = "*" if element.name == 'ul' else "."
        for li in element.find_all('li', recursive=False):
            content = "".join(html_to_adoc(child, in_gray_box) for child in li.children)
            result += f"{symbol} {content.strip()}\n"
        result += "\n"
    # 严格遵守：LaTeX 使用 stem:[ ]
    elif element.name in ['math', 'annotation'] or 'math' in (element.get('class') or []):
        raw_math = element.get_text().strip().replace('$', '')
        result += f" stem:[{raw_math}] "
    # 加粗/斜体
    elif element.name in ['strong', 'b']:
        result += f"*{''.join(html_to_adoc(child, in_gray_box) for child in element.children)}*"
    elif element.name in ['em', 'i']:
        result += f"_{''.join(html_to_adoc(child, in_gray_box) for child in element.children)}_"
    # 表格
    elif element.name == 'table':
        result += "|===\n"
        for tr in element.find_all('tr'):
            cells = tr.find_all(['td', 'th'])
            line = " | ".join("".join(html_to_adoc(c, in_gray_box) for c in cell.children).strip() for cell in cells)
            result += f"| {line}\n"
        result += "|===\n\n"
    else:
        for child in element.children:
            result += html_to_adoc(child, in_gray_box)

    return result


def get_formatted_info(soup):
    """
    改进的标题解析逻辑：
    1. 优先抓取 h1 标签
    2. 使用空格分隔内部 span，防止数字和文本粘连 (如 '2.3The' 变成 '2.3 The')
    3. 解析数字并补零
    """
    # 寻找主标题标签
    title_tag = soup.find('h1', class_='os-title') or \
                soup.find('h1', {'data-type': 'document-title'}) or \
                soup.find('div', class_='os-title-container') or \
                soup.find('h1')

    if not title_tag:
        raw_title = "0.0 Untitled"
    else:
        # 关键点：get_text(" ") 会在子元素之间加空格，解决粘连问题
        raw_title = title_tag.get_text(" ", strip=True)

    # 正则表达式：查找 数字.数字 结构
    # 捕获组1: 章节 (补零用) | 捕获组2: 节号 | 捕获组3: 标题文本
    match = re.search(r'(\d+)\.(\d+)\s*(.*)', raw_title)

    if match:
        chapter = match.group(1).zfill(3)  # 2 -> 002
        section = match.group(2)
        title_text = match.group(3).strip()
        formatted_name = f"{chapter}-{section} (pure) {title_text}"
    else:
        # 如果实在没找到数字，保留原样
        formatted_name = raw_title

    # 过滤掉文件名不支持的字符
    safe_name = re.sub(r'[\\/*?:"<>|]', "", formatted_name)

    # 构造文档头
    header = f"= {formatted_name}\n" \
             f":toc: left\n" \
             f":toclevels: 3\n" \
             f":sectnums:\n" \
             f":stylesheet: ../../myAdocCss.css\n\n" \
             f"'''\n\n"

    return safe_name, header


def run_scraper():
    print("=== OpenStax 标题深度修复工具 ===")
    print("支持：← ↑ → ↓ 箭头, stem:[ ] 公式, 自动补零命名。")
    print("退出：Ctrl + Z 然后回车。")

    save_directory = r"C:\phpStorm_proj\02_myself_ID_EGO\03_English\+ AP American Government 4e  textbook 美国政府（第4版）"

    while True:
        try:
            print("-" * 60)
            url = input("请输入网页地址: ").strip()
            if not url: continue

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            # 解析标题与文件名
            file_name, adoc_header = get_formatted_info(soup)
            save_path = os.path.join(save_directory, f"{file_name}.adoc")

            # 解析正文
            content_area = soup.find('div', {'data-type': 'page'}) or soup.find('main')
            if not content_area:
                print("❌ 错误：未能识别正文内容，请检查网址。")
                continue

            print(f"正在分析并格式化: {file_name}")
            body_adoc = html_to_adoc(content_area)

            # 保存
            os.makedirs(save_directory, exist_ok=True)
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(adoc_header + body_adoc.strip())

            print(f"✅ 处理完成！已保存为：\n{save_path}")

        except EOFError:
            print("\n程序正常退出。再见！")
            break
        except Exception as e:
            print(f"❌ 运行中出现错误: {e}")


if __name__ == "__main__":
    run_scraper()


# 把html网页源代码, 即html上的字体加粗, 各种列表, 等等, 变成asciidoc格式的文件. 比如, 读取C:\Users\priest\Desktop\html.html 文件, 将其内容及里面的字体加粗, 列表等格式, 变成 asciidoc文件的格式代码, 存储为C:\Users\priest\Desktop\asciidoc.adoc 文件

from bs4 import BeautifulSoup

def html_to_asciidoc(html_text):
    soup = BeautifulSoup(html_text, "html.parser")

    def convert_tag(tag):
        """把 HTML 标签转换为 AsciiDoc 字符串"""

        # --- 标题 h1~h6 ---
        if tag.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(tag.name[1])
            prefix = "=" * level
            return f"{prefix} {tag.get_text(strip=True)}\n\n"

        # --- 加粗 strong / b ---
        if tag.name in ["strong", "b"]:
            return f"*{tag.get_text(strip=True)}*"

        # --- 斜体 em / i ---
        if tag.name in ["em", "i"]:
            return f"_{tag.get_text(strip=True)}_"

        # --- 链接 a ---
        if tag.name == "a":
            text = tag.get_text(strip=True)
            url = tag.get("href", "")
            return f"link:{url}[{text}]"

        # --- 段落 p ---
        if tag.name == "p":
            return f"{tag.get_text()}\n\n"

        # --- 无序列表 ul -> li ---
        if tag.name == "ul":
            lines = []
            for li in tag.find_all("li", recursive=False):
                lines.append(f"* {li.get_text()}")
            return "\n".join(lines) + "\n\n"

        # --- 有序列表 ol -> li ---
        if tag.name == "ol":
            lines = []
            for li in tag.find_all("li", recursive=False):
                lines.append(f". {li.get_text()}")
            return "\n".join(lines) + "\n\n"

        return ""

    # 遍历 body 并转换
    output = []

    for element in soup.body.descendants:
        if element.name:
            txt = convert_tag(element)
            if txt:
                output.append(txt)

    return "".join(output)


# ---------------------------
# 主程序：读取 HTML → 转换 → 保存
# ---------------------------

# 公司电脑
# input_path = r"C:\Users\priest\Desktop\html.html"
# output_path = r"C:\Users\priest\Desktop\asciidoc.adoc"

#家里电脑
input_path = r"C:\Users\\mvpri\Desktop\html.html"
output_path = r"C:\Users\\mvpri\Desktop\asciidoc.adoc"

with open(input_path, "r", encoding="utf-8") as f:
    html_content = f.read()

asciidoc_content = html_to_asciidoc(html_content)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(asciidoc_content)

print("转换完成！已输出：", output_path)

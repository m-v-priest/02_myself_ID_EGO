



'''









def create_adoc_files():
    base_filename = "American Pageant - "
    template = """\
= {title}
:toc: left
:toclevels: 3
:sectnums:
:stylesheet: myAdocCss.css

'''

== 释义


'''


== 中文翻译


'''


== pure


'''
"""

    for i in range(1, 60):
        # 格式化数字为3位数，前面补零
        num_str = f"{i:03d}"
        filename = f"{base_filename}{num_str}.adoc"
        title = f"{base_filename}{num_str}"

        # 用格式化后的标题填充模板
        content = template.format(title=title)

        # 写入文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"已创建文件: {filename}")


if __name__ == "__main__":
    create_adoc_files()
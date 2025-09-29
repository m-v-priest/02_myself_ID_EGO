import os
import re


def remove_chinese_translations(content):
    """
    删除ADOC内容中的所有中文翻译部分
    保留英文标题和英文内容，删除中文标题和中文内容
    """
    # 匹配模式：英文标题 -> 英文内容 -> 中文标题 -> 中文内容
    # 使用非贪婪匹配确保只匹配到下一个标题或文件结束
    pattern = r'(\n== [^\n]+)(.*?)(\n\n[^\n]*[\u4e00-\u9fff]+.*?)(?=\n\n== |\Z)'

    # 使用re.DOTALL使.匹配换行符
    new_content = re.sub(
        pattern,
        r'\1\2',
        content,
        flags=re.DOTALL
    )

    # 处理文件末尾的情况（最后一个文章块）
    new_content = re.sub(
        r'(\n== [^\n]+)(.*?)(\n\n[^\n]*[\u4e00-\u9fff]+.*?)\Z',
        r'\1\2',
        new_content,
        flags=re.DOTALL
    )

    return new_content


def process_directory(directory):
    """处理目录中的所有ADOC文件"""
    for filename in os.listdir(directory):
        if filename.endswith('.adoc'):
            file_path = os.path.join(directory, filename)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 删除中文翻译
            new_content = remove_chinese_translations(content)

            # 创建新文件名（保留原文件名）
            new_filename = f"modified_{filename}"
            new_file_path = os.path.join(directory, new_filename)

            # 写入新文件
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"处理完成: {filename} -> {new_filename}")


# 指定目录路径
directory_path = r'C:\Users\priest\Desktop\新建文件夹3'
process_directory(directory_path)
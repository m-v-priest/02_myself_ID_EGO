

import os


def process_text_file(input_path, output_path):
    # 读取文件
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 按段落分割（假设每个段落由空行分隔）
    paragraphs = content.strip().split('\n\n')

    processed_paragraphs = []

    for i, paragraph in enumerate(paragraphs):
        # 找到中英文的分隔位置
        if '。' in paragraph or '？' in paragraph or '，' in paragraph:  # 检测中文字符
            # 查找中文开始的位置
            lines = paragraph.split('\n')

            # 假设每个段落都是英文在前，中文在后
            if len(lines) >= 2:
                # 重新组合，在英文和中文之间添加空行和[.my2]
                english_part = lines[0]
                chinese_parts = lines[1:]  # 处理可能的多行中文
                chinese_part = '\n'.join(chinese_parts)

                processed_paragraph = f"{english_part}\n\n[.my2]\n{chinese_part}"
                processed_paragraphs.append(processed_paragraph)
            else:
                # 如果只有一行，保持原样
                processed_paragraphs.append(paragraph)
        else:
            # 如果没有中文，保持原样
            processed_paragraphs.append(paragraph)

    # 用两个换行符重新连接所有段落
    new_content = '\n\n'.join(processed_paragraphs)

    # 写入新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"文件已处理完成，保存到: {output_path}")


# 使用示例
if __name__ == "__main__":
    input_file = r"C:\Users\mvpri\Desktop\000.txt"

    # 创建输出文件名（在原始文件名后添加_processed）
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_processed{ext}"

    process_text_file(input_file, output_file)
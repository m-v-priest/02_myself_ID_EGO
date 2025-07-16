import re
from pathlib import Path


def extract_and_center_sentences(input_file):
    # 读取文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正则表达式匹配所有以"- (数字.)"开头的句子行
    pattern = r'^-\s*\((\d+\.)\)\s+(.*?)$'
    sentences = re.findall(pattern, content, re.MULTILINE)

    # 去重处理
    unique_sentences = {}
    for num, text in sentences:
        # 保留原始编号格式
        if num not in unique_sentences:
            unique_sentences[num] = text

    # 重新组合句子
    output_lines = []
    for num, text in unique_sentences.items():
        # 原始格式：- (001.) 句子内容
        original_line = f"- ({num}) {text}"

        # 居中处理 - 80字符宽度
        centered_line = center_text(original_line, 80)
        output_lines.append(centered_line)

    # 创建输出文件路径
    output_file = input_file.parent / f"centered_{input_file.name}"

    # 写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(output_lines))  # 句子间加空行分隔

    return output_file, len(unique_sentences)


def center_text(text, width):
    """将文本居中放置在指定宽度内"""
    # 计算左右空格数
    padding_left = (width - len(text)) // 2
    padding_right = width - len(text) - padding_left

    # 创建居中文本
    return " " * padding_left + text + " " * padding_right


if __name__ == "__main__":
    # 设置文件路径
    input_path = Path.home() / "Desktop" / "001.txt"

    # 检查文件是否存在
    if not input_path.exists() or not input_path.is_file():
        print(f"错误: 无法找到文件 {input_path}")
        input("按Enter键退出...")
        exit(1)

    print(f"开始处理文件: {input_path}")
    output_path, count = extract_and_center_sentences(input_path)

    print(f"\n处理完成!")
    print(f"提取并居中处理了 {count} 个独特的英文句子")
    print(f"新文件已保存为: {output_path}")
    input("按Enter键退出...")
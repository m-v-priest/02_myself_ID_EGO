import os
import re


def renumber_sentences(input_file, output_file):
    # 读取原始文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式分割句子（以"- "开头）
    sentences = re.split(r'(?m)^- ', content)
    sentences = [s.strip() for s in sentences if s.strip()]

    # 重新编号
    renumbered = []
    counter = 1
    for sentence in sentences:
        # 移除原有的数字编号（如果有）
        cleaned_sentence = re.sub(r'^\d+\.\s*', '', sentence)
        # 添加新的编号
        renumbered.append(f"- {counter}. {cleaned_sentence}")
        counter += 1

    # 写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(renumbered))


# 文件路径
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
input_path = os.path.join(desktop, 'all.txt')
output_path = os.path.join(desktop, 'all_renumbered.txt')

# 执行函数
renumber_sentences(input_path, output_path)
print(f"重新编号完成，结果已保存到 {output_path}")
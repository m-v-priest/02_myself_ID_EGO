

import re


def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
            open(output_path, 'w', encoding='utf-8') as outfile:

        for line in infile:
            line = line.strip()
            if not line:  # 跳过空行
                continue

            # 提取单词部分（冒号或【前的所有内容）
            word_match = re.match(r'^([^:【]+)', line)
            if not word_match:
                continue

            word = word_match.group(1).strip()

            # 写入单词重复三遍
            for _ in range(3):
                outfile.write(f"{word} +\n")

            # 提取所有例句（▶开头的部分）
            examples = re.findall(r'▶([^▶]+)', line)

            # 处理每个例句
            for example in examples:
                # 移除中文解释部分（括号及其内容）
                eng_example = re.sub(r'\s*\([^)]*\)', '', example).strip()

                # 写入英文例句重复两遍
                for _ in range(2):
                    outfile.write(f"▶{eng_example} +\n")

            # 添加分隔符
            outfile.write("'''\n\n")


# 文件路径
input_file = r'C:\phpStorm_proj\02_myself_ID_EGO\03_English\word_雅思词汇真经\word_雅思词汇真经(豆包AI朗读版)\纯例句.txt'
output_file = r'C:\phpStorm_proj\02_myself_ID_EGO\03_English\word_雅思词汇真经\word_雅思词汇真经(豆包AI朗读版)\processed_纯例句.txt'

# 处理文件
process_file(input_file, output_file)
print(f"处理完成！新文件已保存至: {output_file}")
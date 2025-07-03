
'''

对桌面上000文件夹中的所有adoc文件, 执行以下操作:

比如有:

- 纯英文句子
- 带中文释义的该英文句子

变成:

- 纯英文句子
[.my1]
.案例
====
- 带中文释义的该英文句子
====

'''


import os
import re
from pathlib import Path


def process_adoc_files(folder_path):
    # 获取文件夹中的所有.adoc文件
    adoc_files = [f for f in folder_path.iterdir() if f.is_file() and f.suffix == '.adoc']

    if not adoc_files:
        print(f"在文件夹 {folder_path} 中没有找到.adoc文件")
        return

    print(f"找到 {len(adoc_files)} 个.adoc文件待处理...")

    for file_path in adoc_files:
        print(f"\n正在处理文件: {file_path.name}")

        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 使用正则表达式来匹配内容结构
            sections = re.split(r'==\s*释义\s*|\'{3,}\s*==\s*pure\s*', content)

            if len(sections) < 3:
                print(f"  文件结构不符合要求，跳过处理: {file_path.name}")
                continue

            # 提取释义部分（带中文注解释义的句子）
            definition_section = sections[1].strip()
            # 提取pure部分（纯英文句子）
            pure_section = sections[2].strip()

            # 处理释义部分 - 保留原始编号格式
            definition_items = []
            for match in re.finditer(r'-\s*(\d+\..+?)\+', definition_section, re.DOTALL):
                # 整个句子，包括原始编号
                full_sentence = match.group(1).strip()

                # 提取编号部分但不修改
                # 使用partition分割数字后的点后面的部分
                num_part, sep, sentence_text = full_sentence.partition('.')
                if sep:  # 如果有分隔点
                    # 保留原始编号格式（例如 "7." 或 "7.1")
                    full_num = f"{num_part}{sep}"  # 例如 "7."
                else:
                    # 如果找不到分隔点，保留整个匹配项为编号
                    full_num = full_sentence
                    sentence_text = ""

                # 添加到定义项列表
                definition_items.append((full_num, sentence_text.strip()))

            # 处理pure部分 - 保留原始编号格式
            pure_items = []
            for match in re.finditer(r'-\s*(\d+\..+?)$', pure_section, re.MULTILINE | re.DOTALL):
                # 整个句子，包括原始编号
                full_sentence = match.group(1).strip()

                # 提取编号部分但不修改
                # 使用partition分割数字后的点后面的部分
                num_part, sep, sentence_text = full_sentence.partition('.')
                if sep:  # 如果有分隔点
                    # 保留原始编号格式（例如 "7." 或 "7.1")
                    full_num = f"{num_part}{sep}"  # 例如 "7."
                else:
                    # 如果找不到分隔点，保留整个匹配项为编号
                    full_num = full_sentence
                    sentence_text = ""

                # 添加到纯英文项列表
                pure_items.append((full_num, sentence_text.strip()))

            # 创建新内容
            new_content = []
            for full_num, pure_text in pure_items:
                # 添加纯英文句子，保持原始编号格式
                new_content.append(f"- {full_num} {pure_text}\n\n")

                # 查找对应的释义句子
                def_text = next((text for num, text in definition_items if num == full_num), None)

                if def_text:
                    # 添加案例块
                    new_content.append("[.my1]\n")
                    new_content.append(".案例\n")
                    new_content.append("====\n")
                    # 添加带注释的句子，保持原始编号格式
                    new_content.append(f"- {full_num} {def_text}\n\n")
                    new_content.append("====\n\n")
                else:
                    print(f"  警告: 编号 {full_num} 的句子在释义部分找不到对应的句子")

            # 创建新文件名
            new_filename = f"new_{file_path.name}"
            new_file_path = file_path.parent / new_filename

            # 写入新文件
            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_content)

            print(f"  已创建处理后的文件: {new_filename}")

        except Exception as e:
            print(f"  处理文件 {file_path.name} 时出错: {str(e)}")


if __name__ == "__main__":
    # 设置文件夹路径为桌面上的000文件夹
    desktop = Path.home() / "Desktop"
    target_folder = desktop / "000"

    # 检查文件夹是否存在
    if not target_folder.exists() or not target_folder.is_dir():
        print(f"错误: 无法找到文件夹 {target_folder}")
        input("按Enter键退出...")
        exit(1)

    print(f"开始处理文件夹: {target_folder}")
    process_adoc_files(target_folder)

    print("\n所有文件处理完成! 新文件已保存到原文件夹，文件名以'new_'开头")
    input("按Enter键退出...")
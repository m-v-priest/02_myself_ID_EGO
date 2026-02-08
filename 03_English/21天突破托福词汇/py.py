import os
import re


def process_adoc_files(directory):
    # 切换到目标目录
    if not os.path.exists(directory):
        print(f"错误：找不到目录 {directory}")
        return

    # 匹配编号行的正则表达式，例如 (0001)→ abandon
    # \(\d+\) 匹配括号内的数字，→ 是你指定的箭头符号
    pattern_header = re.compile(r'^\(\d+\)→')

    # 遍历目录下所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.adoc'):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, filename.replace('.adoc', '.txt'))

            extracted_lines = []

            with open(input_path, 'r', encoding='utf-8') as f:
                for line in f:
                    clean_line = line.strip()

                    # 规则 1: 保留编号行
                    if pattern_header.match(clean_line):
                        extracted_lines.append(clean_line + '\n')

                    # 规则 2: 保留以 .. 开头的行
                    elif clean_line.startswith('..'):
                        extracted_lines.append(clean_line + '\n')

                    # 规则 3: 保留分割线 '''
                    elif clean_line == "'''":
                        extracted_lines.append('\n' + clean_line + '\n\n')

            # 将提取的内容写入新的 txt 文件
            with open(output_path, 'w', encoding='utf-8') as f_out:
                f_out.writelines(extracted_lines)

            print(f"处理完成: {filename} → {os.path.basename(output_path)}")


if __name__ == "__main__":
    target_dir = r'C:\Users\mvpri\Desktop\000'
    process_adoc_files(target_dir)
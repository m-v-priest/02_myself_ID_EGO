import os
import re


def fix_plus_positions(content):
    """
    修正adoc文件中加号的位置
    规则：只有当一个人说话结束时，才在最后一行末尾添加加号
    """
    # 分割成行并保留行尾换行符
    lines = content.splitlines(keepends=True)

    # 处理每行内容
    output_lines = []
    current_speaker_lines = []  # 存储当前说话人的所有行
    speaker_pattern = re.compile(r'^[A-Za-z]+:')  # 匹配说话人标识

    for line in lines:
        # 检查是否是说话人开头行
        if speaker_pattern.match(line):
            # 处理上一个说话人的内容
            if current_speaker_lines:
                # 移除所有中间行的加号
                for i in range(len(current_speaker_lines) - 1):
                    current_speaker_lines[i] = current_speaker_lines[i].rstrip().rstrip('+') + '\n'

                # 在最后一行添加加号（如果还没有）
                last_line = current_speaker_lines[-1]
                if not last_line.rstrip().endswith('+'):
                    stripped = last_line.rstrip()
                    if stripped:
                        # 保留原有换行符，在内容后添加加号
                        current_speaker_lines[-1] = stripped + ' +\n'

                output_lines.extend(current_speaker_lines)
                current_speaker_lines = []

            # 开始新说话人
            current_speaker_lines.append(line)
        else:
            # 继续当前说话人的内容
            current_speaker_lines.append(line)

    # 处理最后一个说话人
    if current_speaker_lines:
        for i in range(len(current_speaker_lines) - 1):
            current_speaker_lines[i] = current_speaker_lines[i].rstrip().rstrip('+') + '\n'

        last_line = current_speaker_lines[-1]
        if not last_line.rstrip().endswith('+'):
            stripped = last_line.rstrip()
            if stripped:
                current_speaker_lines[-1] = stripped + ' +\n'

        output_lines.extend(current_speaker_lines)

    return ''.join(output_lines)


def process_directory(directory):
    """处理目录中的所有adoc文件"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.adoc'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                fixed_content = fix_plus_positions(content)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)

                print(f"已修复: {file_path}")


# 要处理的目录
target_directory = r'C:\Users\priest\Desktop\00'

# 执行修复
process_directory(target_directory)
print("所有adoc文件已修复完成！")
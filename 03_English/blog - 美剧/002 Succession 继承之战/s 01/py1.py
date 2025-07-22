def convert_subtitles(input_path, output_path):
    # 读取输入文件
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每行内容
    output_lines = []
    for line in lines:
        # 移除行尾换行符并分割中英文字幕
        if '\\N' in line:
            chinese, english = line.strip().split('\\N', 1)
        else:
            # 对于不带\N的行，保留原样
            chinese = line.strip()
            english = ""

        # 构建新的输出格式
        output_lines.append(english)
        output_lines.append("[.my2]")
        output_lines.append(chinese)
        output_lines.append("")  # 添加空行分隔每组字幕

    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(output_lines))


# 使用示例
if __name__ == "__main__":
    input_file = "C:/Users/priest/Desktop/1.txt"
    output_file = "C:/Users/priest/Desktop/2.txt"  # 新的输出文件名

    convert_subtitles(input_file, output_file)
    print(f"文件转换完成，结果已保存至: {output_file}")
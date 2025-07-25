def convert_subtitle_format(input_file, output_file):
    # 读取原始文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 准备输出内容
    output_content = ['{\n']
    pure_english = []

    for line in lines:
        line = line.strip()
        if '\\N' in line:
            chinese, english = line.split('\\N', 1)
            chinese = chinese.strip()
            english = english.strip()

            # 添加到主输出内容
            output_content.append(f"{english}\n\n[.my2]\n{chinese}\n\n")

            # 添加到纯英文部分
            pure_english.append(english)

    # 添加纯英文部分，用"+"连接
    output_content.append("\n'''\n\n== pure\n\n")
    output_content.append(' +\n'.join(pure_english) + ' +\n')
    output_content.append('}\n')

    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_content)


# 使用示例
input_file = r'C:\Users\priest\Desktop\1.txt'
output_file = r'C:\Users\priest\Desktop\converted_output.txt'
convert_subtitle_format(input_file, output_file)

print(f"转换完成，结果已保存到 {output_file}")
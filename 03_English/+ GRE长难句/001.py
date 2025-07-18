def transform_file(input_path, output_path):
    # 读取原始文件内容
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()

    # 分割内容到两个主要部分
    def find_section_index(header):
        return next((i for i, line in enumerate(content) if line.strip() == header), -1)

    idx_definition = find_section_index("== 释义")
    idx_translation = find_section_index("== 带单词翻译的句子")

    if idx_definition == -1 or idx_translation == -1:
        raise ValueError("未找到必需的标题部分")

    # 解析原始句子
    original_sentences = {}
    for line in content[idx_definition + 1: idx_translation]:
        if line.startswith("- (") and '.）' not in line:
            parts = line.split('.', 1)
            if len(parts) < 2:
                continue
            num_str = parts[0][3:]  # 移除"- ("
            if ')' in num_str:
                num = num_str.split(')')[0]
                original_sentences[num] = line  # 保留完整行

    # 解析带单词翻译的句子
    translated_sentences = {}
    for line in content[idx_translation + 1:]:
        if line.startswith("- (") and '.）' not in line:
            parts = line.split('.', 1)
            if len(parts) < 2:
                continue
            num_str = parts[0][3:]
            if ')' in num_str:
                num = num_str.split(')')[0]
                translated_sentences[num] = line  # 保留完整行

    # 构建新内容
    new_content = ["== 释义"]
    for num in sorted(original_sentences.keys(), key=int):
        new_content.append(original_sentences[num])
        new_content.append("[.my1]")
        new_content.append(".案例")
        new_content.append("====")
        new_content.append(translated_sentences.get(num, f"- ({num}.) 翻译缺失"))
        new_content.append("该句的中文翻译")  # 占位符，实际使用时需要填入真实翻译
        new_content.append("====")
        new_content.append("")  # 空行分隔

    # 写入新文件
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(new_content))


# 使用示例
if __name__ == "__main__":
    input_file = "C:/Users/priest/Desktop/001.txt"
    output_file = "C:/Users/priest/Desktop/002.txt"  # 新的输出文件名

    transform_file(input_file, output_file)
    print(f"文件转换完成，结果已保存至: {output_file}")
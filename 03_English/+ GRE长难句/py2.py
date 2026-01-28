import re
import os


def process_sentences():
    # 文件路径
    input_path = r'C:\Users\priest\Desktop\txt.txt'
    output_path = r'C:\Users\priest\Desktop\输出.txt'

    # 1. 读取原始文件内容
    if not os.path.exists(input_path):
        print(f"错误：找不到文件 {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. 提取所有的“案例”代码块
    # 我们使用“模具”（正则）来抓取从 [.my1] 开始到 ==== 结束的内容
    # 并通过其中的编号 (如 001) 作为索引
    case_blocks = {}
    # 匹配模式：[.my1] ... ==== 之间的所有内容
    case_pattern = re.compile(r'(\[\.my1\].*?\.案例\n====\n- \((\d+)\.\).*?====)', re.DOTALL)

    for match in case_pattern.finditer(content):
        full_block = match.group(1)  # 整个案例块
        index = match.group(2)  # 提取出的编号，例如 001
        case_blocks[index] = full_block

    # 3. 提取“带单词翻译的句子”部分
    # 我们先定位到这个区域，然后提取每一行
    try:
        translation_section = content.split("== 带单词翻译的句子")[1]
    except IndexError:
        print("错误：文件中未找到 '== 带单词翻译的句子' 标记")
        return

    # 提取格式为 - (001.) xxx 的行
    trans_line_pattern = re.compile(r'(- \((\d+)\.\) .*)')
    trans_lines = trans_line_pattern.findall(translation_section)

    # 4. 组合内容
    final_output = []
    for line_text, index in trans_lines:
        # 如果在之前的“仓库”里找到了对应编号的案例块，就组合它们
        if index in case_blocks:
            combined = f"{line_text}\n\n{case_blocks[index]}"
            final_output.append(combined)

    # 5. 写入到输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(final_output))

    print(f"处理完成！请查看桌面上的：输出.txt")


if __name__ == "__main__":
    process_sentences()
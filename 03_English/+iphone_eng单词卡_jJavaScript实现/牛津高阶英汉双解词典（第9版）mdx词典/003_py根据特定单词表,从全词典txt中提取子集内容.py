import os


def extract_words(dictionary_file, word_list_file, output_file):
    """
    根据词头表从词典文件中提取指定单词的完整内容

    参数:
        dictionary_file: 牛津词典文件路径
        word_list_file: 词头表文件路径
        output_file: 输出文件路径
    """
    # 读取词头表
    with open(word_list_file, 'r', encoding='utf-8') as f:
        word_list = [line.strip().lower() for line in f if line.strip()]

    # 创建单词集合用于快速查找
    word_set = set(word_list)
    print(f"词头表中共有 {len(word_set)} 个单词")

    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # 打开词典文件
        with open(dictionary_file, 'r', encoding='utf-8') as dict_f:
            current_word = None
            current_content = []
            in_word_block = False
            found_words = set()

            # 逐行处理词典文件
            for line in dict_f:
                stripped_line = line.strip()

                # 检测单词块开始
                if stripped_line == '</>':
                    if in_word_block and current_word and current_word.lower() in word_set:
                        # 保存找到的单词内容
                        out_f.write(''.join(current_content))
                        found_words.add(current_word.lower())

                    # 重置状态
                    current_word = None
                    current_content = [line]  # 包含起始的</>
                    in_word_block = True
                    continue

                # 在单词块中
                if in_word_block:
                    current_content.append(line)

                    # 检测单词行（紧跟在</>后的第一行）
                    if current_word is None and stripped_line:
                        current_word = stripped_line

            # 处理最后一个单词块
            if in_word_block and current_word and current_word.lower() in word_set:
                out_f.write(''.join(current_content))
                found_words.add(current_word.lower())

    # 检查未找到的单词
    missing_words = word_set - found_words
    if missing_words:
        print(f"警告: 未找到 {len(missing_words)} 个单词")
        with open("missing_words.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted(missing_words)))

    print(f"成功提取 {len(found_words)} 个单词到 {output_file}")


if __name__ == '__main__':
    # 文件路径
    dictionary_file = r"D:\牛津词典\牛津高阶英汉双解词典（第9版）.txt"
    word_list_file = r"D:\牛津词典\词头表.txt"
    output_file = r"D:\牛津词典\提取的单词.txt"

    # 确保文件存在
    for file in [dictionary_file, word_list_file]:
        if not os.path.exists(file):
            print(f"错误: 文件不存在 - {file}")
            exit(1)

    # 提取单词
    extract_words(dictionary_file, word_list_file, output_file)
import os


def read_words(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    lowercase_set = {word.lower() for word in words}
    return lowercase_set, words


def main():
    # 使用正斜杠路径避免转义问题
    existing_file = "C:/Users/priest/Desktop/02_已使用的单词.txt"
    all_list_file = "C:/Users/priest/Desktop/01_all单词表.txt"
    output_file = "C:/Users/priest/Desktop/03_未用到的单词.txt"

    # 读取文件内容
    existing_set, _ = read_words(existing_file)
    _, all_words = read_words(all_list_file)

    # 过滤出未使用的单词
    unused_words = [word for word in all_words if word.lower() not in existing_set]

    # 写入新文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(unused_words))

    print(f"处理完成！未使用的单词已保存至: {output_file}")
    print(f"原始单词数量: {len(all_words)}，未使用单词数量: {len(unused_words)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"处理过程中出错: {str(e)}")
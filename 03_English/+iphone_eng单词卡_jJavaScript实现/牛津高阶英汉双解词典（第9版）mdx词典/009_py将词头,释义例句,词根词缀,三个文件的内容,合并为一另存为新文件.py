

'''

我有三个txt文件.

第1个文件的地址:

C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\txt_03雅思词汇真经词头表.txt

这个文件中, 每一行, 都是一个英语单词 (这块内容, 我们称为A部分)

第2个文件的地址是:

C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\txt_05雅思词汇真经单词pure.txt

这个文件中, 每个英语单词前用あ符号表示. 比如

あ【abandon】
... (这里的省略号表示跟在后面的内容)
...
...
あ【abdomen】
...
...


上面就表示有两个单词. 即, 两个あ之间的内容, 就是一个单词的完整内容, 包括中英文释义, 例句等等. (这块内容, 我们称为B部分)


第3个文件的地址是:

C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\txt_06雅思词汇真经_词根词缀.txt

存放着每个单词的词根词缀内容. 比如

〖oxygen〗 词根词缀: oxy- (尖, 酸) + gen- (生成)
〖oxide〗 词根词缀: ox- (氧) + ide (化合)

单词名字是写在〖 〗 中间的.

(这块词根词缀内容, 我们称为C部分)



你来编写一个python程序. 执行以下功能:

先读取 txt_03雅思词汇真经词头表 文件中的所有单词, 然后针对每一个单词(即A部分), 都到 "txt_05雅思词汇真经单词pure"文件中去查找该单词相应的完整内容(即B部分), 如果没找到,就用一个"ない"代替. 再到"txt_06雅思词汇真经_词根词缀"文件中去查找该单词相应的词根词缀内容(即C部分),就用"ない"代替.

把找到的内容, 按照下面的格式, 存到一个新的txt文件中.

格式为:
id号	单词1的 A部分	B部分	C部分
id号	单词2的 A部分	B部分	C部分
id号	单词3的 A部分	B部分	C部分
...

每个单词的id号, 请递增, 编号从1开始.

即, 每个单词有4块内容: id号, A部分, B部分,C部分
这4块内容,是用制表符来分隔开的.

'''








import re

# 文件路径
word_list_file = r"C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\txt_03雅思词汇真经词头表.txt"
b_content_file = r"C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\txt_05雅思词汇真经单词pure.txt"
c_content_file = r"C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\txt_06雅思词汇真经_词根词缀.txt"
output_file = r"C:\+myGithub\02_myself_ID_EGO\03_English\+iphone_eng单词卡_jJavaScript实现\牛津高阶英汉双解词典（第9版）mdx词典\combined_output.txt"

def read_word_list(file_path):
    """读取词头表文件，返回单词列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def parse_b_content(file_path):
    """解析B部分内容，返回字典{单词: 完整内容}"""
    content_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式匹配所有单词及其内容
    pattern = r'あ【(.*?)】([\s\S]*?)(?=あ【|$)'
    matches = re.findall(pattern, content)

    for word, content_text in matches:
        # 清理内容：去除首尾空白，替换换行符为空格
        cleaned_content = content_text.strip().replace('\n', ' ')
        content_dict[word] = cleaned_content

    return content_dict

def parse_c_content(file_path):
    """解析C部分内容，返回字典{单词: 词根词缀内容}"""
    content_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # 匹配格式：〖单词〗 词根词缀内容
            match = re.match(r'〖(.*?)〗\s*(.*)', line)
            if match:
                word = match.group(1)
                content = match.group(2).strip()
                content_dict[word] = content
    return content_dict

def main():
    # 读取A部分单词列表
    a_words = read_word_list(word_list_file)

    # 解析B部分内容
    b_dict = parse_b_content(b_content_file)

    # 解析C部分内容
    c_dict = parse_c_content(c_content_file)

    # 创建输出文件
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # 写入标题行
        out_f.write("ID\tA部分\tB部分\tC部分\n")

        # 处理每个单词
        for idx, word in enumerate(a_words, start=1):
            # 获取B部分内容，如果不存在则用"ない"
            b_content = b_dict.get(word, "ない")

            # 获取C部分内容，如果不存在则用"ない"
            c_content = c_dict.get(word, "ない")

            # 写入结果，使用制表符分隔
            out_f.write(f"{idx}\t{word}\t{b_content}\t{c_content}\n")

    print(f"处理完成！共处理了 {len(a_words)} 个单词。")
    print(f"结果已保存至: {output_file}")

if __name__ == "__main__":
    main()
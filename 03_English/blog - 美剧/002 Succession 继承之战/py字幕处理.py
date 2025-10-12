
# 我的地址 ‪C:\Users\mvpri\Documents\从ASS字幕文件提取文本-字云.txt
# 这个txt中, 内容是美剧字幕. 里面的内容片段是下面这样的:
#
# THE SUB-MAN
# 关注新浪微博\N@FIX字幕侠
# m 34 -191 l 162 -6 l 25 191 l 129 191 l 213 69 l 359 277 l 360 277 l 465 277 l 265 -6 l 394 -191 l 290 -191 l 213 -81 l 137 -191 l 34 -191
# 最后成交价
# 最后成交价
# 理查德 能帮我查一下韦斯达的股价吗\NRichard, can you get me the price of the Waystar stock?
# -昨晚休市前的价格  -他怎么样了\N- At close last night, please. - How is he?
# 不错 清醒点了 他还试着穿袜子\NGood. A little clearer. He tried to put on a sock.
# 早\NHey.
# 早\NMorning.
# 早啊 蒙代尔 祝我好运吧伙计\NHey, Mondale. Wish me luck, buddy.
# 祝我好运吧\NWish me luck.
#
#
# 可以看到, 那些带有 \N 字符串的行, 就是字幕行.  \N前面为中文字幕, \N后面为英文字幕.
#
# 你来编写一个python程序, 将所有带有 \N 字符串的行, 后面的英文字幕, 提取出来. 另存到一个新的txt中. 注意, 内容格式要每一行英文字幕都都间隔一个空行, 即要像下面这样:
#
# Richard, can you get me the price of the Waystar stock?
#
# Good. A little clearer. He tried to put on a sock.
#
# Hey, Mondale. Wish me luck, buddy.
#
# Wish me luck.




def extract_english_subtitles_from_subtitle_file(input_file_path, output_file_path):
    """
    从字幕文件中提取英文字幕部分

    参数:
    input_file_path: 输入的字幕文件路径
    output_file_path: 输出的英文字幕文件路径
    """
    try:
        # 读取输入文件
        with open(input_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 提取英文字幕
        english_lines = []
        for line in lines:
            # 检查是否包含 \N 字符串
            if '\\N' in line:
                # 分割中英文部分，取英文部分（\N 后面的部分）
                parts = line.strip().split('\\N')
                if len(parts) >= 2:
                    english_text = parts[1].strip()
                    if english_text:  # 确保英文部分不为空
                        english_lines.append(english_text)

        # 写入输出文件，每行英文字幕之间间隔一个空行
        with open(output_file_path, 'w', encoding='utf-8') as f:
            for i, english_line in enumerate(english_lines):
                f.write(english_line + '\n')
                # 如果不是最后一行，则添加一个空行
                if i < len(english_lines) - 1:
                    f.write('\n')

        print(f"成功提取 {len(english_lines)} 行英文字幕")
        print(f"输出文件已保存为: {output_file_path}")
        return True

    except FileNotFoundError:
        print(f"错误: 找不到文件 {input_file_path}")
        print("请确保文件路径正确，并且文件存在于指定位置。")
        return False
    except Exception as e:
        print(f"处理文件时出错: {e}")
        return False


# 使用方法：
# 请将下面的路径替换为您实际的文件路径
input_file_path = r"C:\Users\mvpri\Documents\从ASS字幕文件提取文本-字云.txt"
output_file_path = r"C:\Users\mvpri\Documents\提取的英文字幕.txt"

# 执行提取
extract_english_subtitles_from_subtitle_file(input_file_path, output_file_path)














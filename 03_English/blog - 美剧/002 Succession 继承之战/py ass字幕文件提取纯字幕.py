import os
import re


def extract_english_subtitles(ass_file_path):
    # 从单个 ASS 文件中提取 \N 后面的英文字幕，并去除所有 ASS 格式标签。
    # 每行字幕后插入一个空行。

    extracted_lines = []
    # 正则表达式用于匹配并去除 ASS 格式标签，如 {\\...}
    ASS_TAG_PATTERN = re.compile(r'\{.*?\}')

    # 文件编码通常是 UTF-8
    try:
        with open(ass_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 1. 筛选出 Dialogue 行
                if line.startswith('Dialogue:'):
                    # 2. ASS 格式中，字幕文本是第10个字段（用9个逗号分隔）
                    #    我们使用 split(',', 9) 来只分割前9次逗号，保留文本部分为最后一个元素
                    parts = line.split(',', 9)

                    if len(parts) > 9:
                        subtitle_text = parts[9].strip()

                        # 3. 检查是否包含双语分隔符 \N
                        if '\\N' in subtitle_text:
                            # 4. 提取 \N 后的英文字幕部分
                            #    使用 split('\\N', 1) 确保只在第一个 \N 处分割
                            try:
                                chinese_text, english_text_with_tags = subtitle_text.split('\\N', 1)
                            except ValueError:
                                # 如果 split 失败（例如，行中没有 \N 或 \N 在行首），则跳过。
                                continue

                                # 5. 去除英文字幕中的所有 ASS 格式标签，如 {\\r原文字幕}
                            clean_english_text = ASS_TAG_PATTERN.sub('', english_text_with_tags).strip()

                            # 6. 如果提取到的纯英文字幕不为空，则添加到列表中，并添加一个空行
                            if clean_english_text:
                                extracted_lines.append(clean_english_text)
                                # 插入一个空行，符合要求
                                extracted_lines.append('')
    except FileNotFoundError:
        print(f"错误: 找不到文件 {ass_file_path}")
    except Exception as e:
        print(f"处理文件 {ass_file_path} 时发生错误: {e}")

    return extracted_lines


def process_directory(directory_path):
    """
    遍历指定目录，处理所有 ASS 文件并保存为 ADOC 文件。
    """
    if not os.path.isdir(directory_path):
        print(f"错误: 目录 '{directory_path}' 不存在或不是有效目录。请检查路径是否正确。")
        return

    print(f"开始处理目录: {directory_path}")

    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.ass'):
            ass_file_path = os.path.join(directory_path, filename)

            # 确定输出文件路径（扩展名改为 .adoc）
            base_name = os.path.splitext(filename)[0]
            adoc_file_name = base_name + '.adoc'
            adoc_file_path = os.path.join(directory_path, adoc_file_name)

            print(f"  -> 正在处理文件: {filename}")

            # 提取字幕
            subtitles = extract_english_subtitles(ass_file_path)

            if subtitles:
                # 将结果写入新的 .adoc 文件，每行末尾自动添加 \n
                # 由于我们已经在列表中添加了空字符串 ('') 作为空行，所以可以直接写入。
                try:
                    with open(adoc_file_path, 'w', encoding='utf-8') as outfile:
                        # 使用 join 方法一次性写入，比多次 append 更高效
                        outfile.write('\n'.join(subtitles))
                    print(f"  -> 成功保存到: {adoc_file_name}")
                except Exception as e:
                    print(f"  -> 错误: 写入文件 {adoc_file_name} 时失败: {e}")
            else:
                print(f"  -> 文件 {filename} 中未找到符合条件的双语字幕。")

    print("所有文件处理完毕。")


# ======================================================================
# 【重要】请将下面的路径替换成您存放 ASS 文件的实际目录地址
# 示例: 如果您的文件在 D:\Subtitles，则应填写 D:\Subtitles
# 注意: 在 Windows 路径中，可以使用双反斜杠 '\\' 或单正斜杠 '/'
# ======================================================================
ASS_DIRECTORY = r"C:\+myGithub\02_myself_ID_EGO\03_English\blog - 美剧\002 Succession 继承之战\【中英字幕】Succession.S01-S04.1080p.BluRay.x265-RARBG\Succession.S04.1080p.WEBRip.x265-RARBG"

if __name__ == "__main__":
    if ASS_DIRECTORY:
        process_directory(ASS_DIRECTORY)
    else:
        print("请在脚本中设置 ASS_DIRECTORY 变量为您的字幕文件目录路径后，再运行脚本。")
import re
import os


def extract_and_format_text(input_filepath, output_filepath):
    """
    从 HTML 文件中提取特定模式的文本，并按指定格式写入新文件。

    Args:
        input_filepath (str): 包含 HTML 代码的输入文件路径。
        output_filepath (str): 结果将写入的输出文件路径。
    """
    try:
        # 1. 读取输入文件内容
        with open(input_filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # 2. 定义正则表达式模式
        # 这个模式查找：
        # - </template> (作为起始标记)
        # - (.*?) (捕获组：非贪婪匹配任何字符，直到下一个标记)
        # - </faceplate-screen-reader-content> (作为结束标记)
        # re.DOTALL (或 re.S) 标志让 '.' 匹配包括换行符在内的所有字符，
        # 确保能捕获多行的内容。
        pattern = r'</template>\s*(.*?)\s*</faceplate-screen-reader-content>'

        # 3. 查找所有匹配项
        # re.findall() 返回所有匹配捕获组 (.*?) 的内容列表
        extracted_texts = re.findall(pattern, html_content, re.DOTALL)

        # 4. 清理并格式化提取出的文本
        formatted_output = ""
        for text in extracted_texts:
            # 清理：去除开头和结尾的空白字符、换行符等，确保只保留核心句子
            cleaned_text = text.strip()

            # 格式化：每个句子后跟两个换行符 (一个用于句子结尾，一个用于空行)
            if cleaned_text:
                formatted_output += cleaned_text + "\n\n"

        # 5. 写入到新的输出文件
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(formatted_output)

        print(f"✅ 文本已成功提取并写入到文件: {output_filepath}")

    except FileNotFoundError:
        print(f"❌ 错误：未找到文件 {input_filepath}。请检查路径是否正确。")
    except Exception as e:
        print(f"❌ 发生了一个错误: {e}")


# --- 配置和运行 ---

# 你的输入文件路径
INPUT_FILE = r"C:\Users\mvpri\Desktop\000\000.html"

# 你希望保存结果的输出文件路径 (可以和输入文件在同一目录下，但文件名不同)
# 这里假设输出文件名为 extracted_content.txt
OUTPUT_FILE = r"C:\Users\mvpri\Desktop\000\extracted_content.txt"

# 运行函数
extract_and_format_text(INPUT_FILE, OUTPUT_FILE)
import os
import re


def process_adoc_files():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    folder_path = os.path.join(desktop, '000')

    for filename in os.listdir(folder_path):
        if filename.endswith('.adoc'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 替换样式表路径
            content = content.replace(':stylesheet: myAdocCss.css',
                                      ':stylesheet: ../../myAdocCss.css')

            # 精确匹配释义段落
            pattern = re.compile(
                r'(== 释义\n+)(.*?)(\n+\'\'\'\n+== 中文翻译)',
                re.DOTALL
            )

            def process_sentences(match):
                header = match.group(1)
                text = match.group(2).strip()
                footer = match.group(3)

                # 核心处理逻辑
                # 1. 分割句子
                sentences = re.split(r'(?<=[.!?])\s+', text)

                # 2. 处理每个句子
                processed = []
                for sent in sentences:
                    # 保留原始换行（如果有）
                    lines = [line.strip() for line in sent.split('\n') if line.strip()]
                    processed_line = ' +\r\n'.join(lines)
                    if processed_line:
                        processed.append(processed_line)

                # 3. 组合处理后的文本
                formatted_text = ' +\r\n'.join(
                    [f"{sentence.rstrip('.!? ')}. +" if not sentence.endswith(('.', '!', '?')) else f"{sentence} +"
                     for sentence in processed]
                )

                return f"{header}{formatted_text}\r\n{footer}"

            content = pattern.sub(process_sentences, content)

            with open(file_path, 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(content)

            print(f"已处理文件: {filename}")


if __name__ == "__main__":
    process_adoc_files()
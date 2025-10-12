import re
import os

def extract_content_from_html(file_path, output_path):
    """
    从HTML文件中提取</template>和</faceplate-screen-reader-content>之间的内容

    Args:
        file_path (str): 输入HTML文件路径
        output_path (str): 输出txt文件路径
    """
    try:
        # 读取HTML文件
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式匹配
        # 匹配完整的 <faceplate-screen-reader-content>...</faceplate-screen-reader-content> 结构
        # 并提取其中模板标签和结束标签之间的内容
        pattern = r'<faceplate-screen-reader-content[^>]*>.*?</template>\s*(.*?)\s*</faceplate-screen-reader-content>'
        matches = re.findall(pattern, content, re.DOTALL)

        # 清理匹配到的内容
        extracted_content = []
        for match in matches:
            # 去除首尾空白字符和多余的空白
            cleaned = re.sub(r'\s+', ' ', match.strip())
            if cleaned:  # 只保留非空内容
                extracted_content.append(cleaned)

        # 将提取的内容写入新文件，每行后跟一个空行
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for item in extracted_content:
                output_file.write(item + '\n\n')

        print(f"提取完成！共找到 {len(extracted_content)} 条内容")
        print(f"结果已保存到: {output_path}")

        # 显示提取的内容
        if extracted_content:
            print("\n提取的内容预览:")
            # 最多显示前10条
            for i, item in enumerate(extracted_content[:10], 1):
                print(f"{i}. {item}")

            if len(extracted_content) > 10:
                print(f"... 还有 {len(extracted_content) - 10} 条内容")
        else:
            print("\n未找到匹配的内容，请检查HTML格式是否符合预期")

        return extracted_content

    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        print("请检查文件路径是否正确")
        return []
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
        return []

def main():
    # 设置输入和输出文件路径（根据您的实际需求修改这些路径）
    input_file = r"C:\\Users\\mvpri\\Desktop\\000\\000.html"
    output_file = r"C:\\Users\\mvpri\\Desktop\\000\\extracted_content.txt"

    print("=" * 50)
    print("HTML内容提取工具")
    print("=" * 50)
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"警告: 输入文件不存在: {input_file}")
        print("\n请确保:")
        print("1. 文件路径正确")
        print("2. 文件确实存在于该路径")
        print("3. 您有读取该文件的权限")
        return

    # 执行提取
    print("\n开始提取内容...")
    result = extract_content_from_html(input_file, output_file)

    if result:
        print("\n" + "=" * 50)
        print("处理完成!")
        print(f"成功提取 {len(result)} 条内容")
        print(f"结果已保存到: {output_file}")
    else:
        print("\n处理完成，但未提取到任何内容")

if __name__ == "__main__":
    main()

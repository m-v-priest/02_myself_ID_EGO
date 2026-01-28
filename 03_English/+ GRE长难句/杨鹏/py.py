import os


def create_adoc_files():
    # 1. 定义目标文件夹路径
    # 使用原始字符串(r'')来处理路径中的反斜杠和空格
    target_dir = r'C:\phpStorm_proj\02_myself_ID_EGO\03_English\+ GRE长难句\杨鹏'

    # 2. 如果文件夹不存在，则创建它
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"检测到目录不存在，已创建目录: {target_dir}")

    # 3. 循环生成 200 个文件
    for i in range(1, 201):
        # 将数字格式化为三位，例如：1 → 001
        num_str = str(i).zfill(3)

        # 定义文件名和完整路径
        file_name = f"{num_str}.adoc"
        file_path = os.path.join(target_dir, file_name)

        # 4. 准备写入的内容
        # 注意：这里我们按照你的要求，让 = 后面的编号与文件名保持一致
        # (修正了你描述中 200.adoc 对应 020 的笔误，统一为 200)
        content = f"""= {num_str}
:toc: left
:toclevels: 3
:sectnums:
:stylesheet: ../../../../myAdocCss.css

'''



'''
"""

        # 5. 写入文件
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"写入文件 {file_name} 时出错: {e}")

    print(f"任务完成！已在目标文件夹中创建了 200 个 .adoc 文件。")


if __name__ == "__main__":
    create_adoc_files()


'''
注意: 运行 本python程序时, 先把这段注释删掉, 否则程序会报错

用户的需求很明确：他们有一个目录C:\Users\priest\Desktop\000，里面有28个txt文件。需要为每个txt文件创建一个同名的adoc文件，扩展名改为.adoc。每个adoc文件的内容模板中，标题行需要与文件名完全一致，但要去掉扩展名，并在前面加上等号。其他部分保持固定结构。
'''


import os


def create_adoc_files():
    # 设置目标目录路径
    target_dir = r'C:\Users\priest\Desktop\000'

    # 遍历目录中所有.txt文件
    for txt_filename in os.listdir(target_dir):
        if txt_filename.endswith('.txt'):
            # 获取基础文件名（不带扩展名）
            base_name = os.path.splitext(txt_filename)[0]

            # 构建.adoc文件名
            adoc_filename = f"{base_name}.adoc"
            adoc_path = os.path.join(target_dir, adoc_filename)

            # 构建文件内容模板
            content = f"""\
= {base_name}
:toc: left
:toclevels: 3
:sectnums:
:stylesheet: ../../../myAdocCss.css

'''

== 释义



'''


== 中文翻译


'''


== pure


'''
"""
            # 写入文件
            with open(adoc_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"已创建文件: {adoc_filename}")


if __name__ == "__main__":
    create_adoc_files()
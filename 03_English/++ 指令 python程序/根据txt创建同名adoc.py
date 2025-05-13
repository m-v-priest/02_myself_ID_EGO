

'''
注意: 执行本 python文件时, 把这个注释先删掉, 才能执行成功

创建一个python程序, 执行以下操作:

在window 10 系统的桌面上, 有一个名叫000的文件夹. 里面有一些 扩展名是 ".txt" 的文本文件.

针对每一个txt文件, 创建一个同名的 扩展名是".adoc"的文本文件.

每一个 ".adoc"文件中, 填入如下内容 (即下面中括号里的内容):

[



= 文件名
:toc: left
:toclevels: 3
:sectnums:
:stylesheet: myAdocCss.css

'''

== 释义

'''

== 中文释义

'''

== pure


'''

]


注意: 上面内容中的"= 文件名", 即等号后面的 "文件名" 这个字符串内容, 要改成该".adoc"文件的文件名. 比如, 如果这个文件名是 "1.01 Ideals of DEMOCRACY.adoc" , 那么这个文件里的"= 文件名"字符串就应该是"= 1.01 Ideals of DEMOCRACY"


'''










import os


def create_adoc_files():
    # 获取桌面路径
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    folder_path = os.path.join(desktop, '000')

    # 检查000文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：桌面上的000文件夹不存在")
        return

    # 遍历000文件夹中的所有txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            # 创建对应的adoc文件名
            base_name = os.path.splitext(filename)[0]
            adoc_filename = base_name + '.adoc'
            adoc_path = os.path.join(folder_path, adoc_filename)

            # 创建adoc文件内容（使用双三引号包裹字符串）
            content = f"""
= {base_name}
:toc: left
:toclevels: 3
:sectnums:
:stylesheet: myAdocCss.css

'''

== 释义

'''

== 中文释义

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
    print("所有.adoc文件已创建完成")
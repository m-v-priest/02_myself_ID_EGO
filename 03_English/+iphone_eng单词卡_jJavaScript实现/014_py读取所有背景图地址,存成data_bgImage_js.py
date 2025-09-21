



'''
编写一个python程序, 读取 C:\Users\mvpri\Desktop\000 目录下的所有文件的文件名, 把它们存入一个新的名叫 data_bgImages.js 的文件中, 内容为:

const data_bgImages = [
"bg_img/bg00001.jpg",
"bg_img/bg00002.jpg",
...
];


比如, 如果000 目录下只有两个文件, 名字叫bg00001.jpg, bg00002.jpg, 则就把这些名字放入上面 "bg_img/"字符后面.

如果data_bgImages.js 已经存在, 就覆盖它. 如果data_bgImages.js不存在, 就创建它.
'''





import os
import glob


def generate_bg_images_js(directory, output_file):
    # 获取目录下所有文件的完整路径
    all_files = glob.glob(os.path.join(directory, '*'))

    # 过滤掉子目录，只保留文件
    files = [f for f in all_files if os.path.isfile(f)]

    # 提取文件名并排序
    filenames = sorted([os.path.basename(f) for f in files])

    # 生成JavaScript数组内容
    js_content = "const data_bgImages = [\n"
    for filename in filenames:
        js_content += f'    "bg_img/{filename}",\n'

    # 移除最后一个逗号
    if js_content.endswith(",\n"):
        js_content = js_content[:-2] + "\n"

    js_content += "];"

    # 写入文件（覆盖已存在文件）
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"成功生成 {output_file}，包含 {len(filenames)} 个文件")


if __name__ == "__main__":
    # 配置参数
    source_directory = r"C:\Users\mvpri\Desktop\000"
    output_js_file = "data_bgImages.js"

    # 执行生成
    generate_bg_images_js(source_directory, output_js_file)
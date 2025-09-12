
# 这个bg_img 目录中, 存放的是每个页面会随机读取的背景图


#
# 编写一个python程序, 执行以下功能:
#
#
# 在 ../bg_img 目录中, 有一堆图片, 扩展名各式各样.
# 读取该目录中的所有图片的名字和扩展名, 把它们存成 JavaScript中的 数组, 返回给我.
#
# 即, 返回的格式如下:
#
# const bgImages = [
#     "bg_img/bg001.png",
#     "bg_img/bg009.avif",
#     "bg_img/bg009.jpg",
#     "bg_img/bg012.webp",
#     ...
# ]
#
# 将返回的这个数组, 存入一个 txt格式文件中, 放在原目录下.

import os
import glob


def get_image_list():
    # 支持的图片扩展名
    image_extensions = ['png', 'jpg', 'jpeg', 'gif', 'webp', 'avif', 'svg', 'bmp']

    # 构建glob模式匹配所有图片文件
    patterns = [f"bg_img/*.{ext}" for ext in image_extensions]

    # 获取所有匹配的文件路径
    image_files = []
    for pattern in patterns:
        image_files.extend(glob.glob(pattern))

    # 对结果进行排序（按文件名）
    image_files.sort()

    # 转换为JavaScript数组格式，并修正路径分隔符
    js_array = "const bgImages = [\n"
    for file in image_files:
        # 将路径中的反斜杠统一替换为正斜杠
        corrected_path = file.replace("\\", "/")
        # 确保路径格式正确
        if corrected_path.startswith("../"):
            corrected_path = corrected_path[3:]  # 移除前面的../
        js_array += f"    \"{corrected_path}\",\n"
    js_array = js_array.rstrip(",\n") + "\n];"

    return js_array


def save_to_file(content, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"成功将图片列表保存到 {filename}")
    except Exception as e:
        print(f"保存文件时出错: {e}")


if __name__ == "__main__":
    js_array = get_image_list()
    output_file = "bg_images.txt"
    save_to_file(js_array, output_file)
    print("\n生成的JavaScript数组内容：")
    print(js_array)
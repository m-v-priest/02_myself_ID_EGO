# html转txt_最终版.py
import os
import time
import logging
from pathlib import Path
import html2text
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def html_to_text_improved(html_file_path, output_dir):
    """
    改进的HTML转文本函数，使用html2text和BeautifulSoup
    """
    try:
        # 读取HTML文件
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # 初始化html2text转换器
        h = html2text.HTML2Text()
        h.ignore_links = False  # 是否忽略链接
        h.ignore_images = True  # 忽略图片
        h.ignore_tables = False  # 不忽略表格
        h.body_width = 0  # 不自动换行
        h.unicode_snob = True  # 使用Unicode字符

        # 使用html2text转换
        text = h.handle(html_content)

        # 进一步使用BeautifulSoup清理
        soup = BeautifulSoup(html_content, 'html.parser')

        # 移除不需要的标签
        for element in soup(['script', 'style', 'meta', 'link', 'noscript']):
            element.decompose()

        # 获取纯文本
        soup_text = soup.get_text(separator='\n', strip=True)

        # 合并两种方法的结果（以html2text为主，因为它的格式更好）
        # 如果html2text结果太短，使用BeautifulSoup的结果
        if len(text.strip()) < 100 and len(soup_text) > len(text):
            final_text = soup_text
        else:
            final_text = text

        # 清理文本：去除多余空行
        lines = []
        for line in final_text.split('\n'):
            line = line.strip()
            if line:  # 只保留非空行
                lines.append(line)

        cleaned_text = '\n'.join(lines)

        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

        # 生成输出文件路径
        filename = Path(html_file_path).stem
        output_path = os.path.join(output_dir, f"{filename}.txt")

        # 保存文本
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        logger.info(f"✓ 已转换: {Path(html_file_path).name}")
        return True, html_file_path

    except UnicodeDecodeError:
        # 尝试其他编码
        try:
            with open(html_file_path, 'r', encoding='gbk') as f:
                html_content = f.read()
            return html_to_text_improved(html_file_path, output_dir)
        except Exception as e:
            logger.error(f"✗ 编码错误: {html_file_path} - {str(e)}")
            return False, html_file_path
    except Exception as e:
        logger.error(f"✗ 转换失败: {html_file_path} - {str(e)}")
        return False, html_file_path


def convert_all_html_files(input_dir, output_dir=None, max_workers=3):
    """
    转换目录下的所有HTML文件

    Args:
        input_dir: 输入目录路径
        output_dir: 输出目录路径（默认为输入目录下的converted_texts）
        max_workers: 最大线程数
    """
    # 检查输入目录
    if not os.path.exists(input_dir):
        logger.error(f"输入目录不存在: {input_dir}")
        return

    # 设置输出目录
    if output_dir is None:
        output_dir = os.path.join(input_dir, "converted_texts")

    # 查找所有HTML文件
    html_files = []
    for root, dirs, files in os.walk(input_dir):
        # 跳过输出目录
        if os.path.abspath(output_dir) in os.path.abspath(root):
            continue

        for file in files:
            if file.lower().endswith(('.html', '.htm')):
                html_files.append(os.path.join(root, file))

    if not html_files:
        logger.warning(f"在目录中未找到HTML文件: {input_dir}")
        return

    logger.info(f"找到 {len(html_files)} 个HTML文件")

    # 使用线程池并行处理
    success_count = 0
    fail_count = 0
    failures = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交任务
        future_to_file = {
            executor.submit(html_to_text_improved, html_file, output_dir): html_file
            for html_file in html_files
        }

        # 处理结果
        for future in as_completed(future_to_file):
            html_file = future_to_file[future]
            try:
                success, result = future.result(timeout=30)
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                    failures.append(result)
            except Exception as e:
                fail_count += 1
                failures.append(f"{html_file}: {str(e)}")
                logger.error(f"✗ 处理异常: {html_file} - {str(e)}")

    # 输出统计
    logger.info("=" * 50)
    logger.info(f"转换完成！")
    logger.info(f"成功: {success_count} 个文件")
    logger.info(f"失败: {fail_count} 个文件")

    if failures:
        logger.warning("失败的文件列表:")
        for failure in failures[:10]:  # 只显示前10个失败
            logger.warning(f"  - {failure}")
        if len(failures) > 10:
            logger.warning(f"  ... 还有 {len(failures) - 10} 个失败文件")


def main():
    """主函数"""
    # 设置输入目录
    input_directory = r"C:\Users\priest\Desktop\000"

    # 设置输出目录（可选，默认会在输入目录下创建converted_texts文件夹）
    output_directory = None  # 使用默认

    # 记录开始时间
    start_time = time.time()

    # 转换文件
    convert_all_html_files(input_directory, output_directory, max_workers=3)

    # 计算耗时
    elapsed_time = time.time() - start_time
    logger.info(f"总耗时: {elapsed_time:.2f} 秒")
    logger.info(f"输出目录: {output_directory or os.path.join(input_directory, 'converted_texts')}")


if __name__ == "__main__":
    main()
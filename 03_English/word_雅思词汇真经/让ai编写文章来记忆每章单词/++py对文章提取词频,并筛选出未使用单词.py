import spacy
from typing import Set, List
import os

# --- 配置部分 ---
# 请确保这些路径与您的文件实际路径一致
#公司电脑用这个路径
# ARTICLE_PATH = "C:\\Users\\priest\\Desktop\\000_已编文章.txt"
# ALL_WORDS_PATH = "C:\\Users\\priest\\Desktop\\01_all单词表.txt"
# USED_WORDS_PATH = "C:\\Users\\priest\\Desktop\\02_已使用的单词.txt"
# UNUSED_WORDS_PATH = "C:\\Users\\priest\\Desktop\\03_未用到的单词.txt"


#家里电脑用这个路径
ARTICLE_PATH = "C:\\Users\\mvpri\\Desktop\\000_已编文章.txt"
ALL_WORDS_PATH = "C:\\Users\\\mvpri\\Desktop\\01_all单词表.txt"
USED_WORDS_PATH = "C:\\Users\\\mvpri\\Desktop\\02_已使用的单词.txt"
UNUSED_WORDS_PATH = "C:\\Users\\\mvpri\\Desktop\\03_未用到的单词.txt"




# 加载 spaCy 模型
# 确保您已经运行了 python -m spacy download en_core_web_sm
try:
    # 尝试加载模型。使用 try-except 是一个好的习惯，以处理模型未找到的情况。
    nlp = spacy.load("en_core_web_sm")
    print("Spacy 模型加载成功：en_core_web_sm")
except OSError:
    print("错误：无法找到 Spacy 模型 'en_core_web_sm'。")
    print("请确保已运行命令：python -m spacy download en_core_web_sm")
    exit()


def read_words_to_set(filepath: str) -> Set[str]:
    """
    读取文件中的单词列表，将每个单词转换为小写并存入集合。
    """
    word_set = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()  # 去除首尾空白并转为小写
                if word:
                    word_set.add(word)
        return word_set
    except FileNotFoundError:
        print(f"警告：未找到文件 {filepath}，将使用空集合。")
        return set()
    except Exception as e:
        print(f"读取文件 {filepath} 时发生错误: {e}")
        return set()


def write_words_from_set(filepath: str, word_set: Set[str]):
    """
    将集合中的单词按字母顺序排序后，一行一个地写入文件。
    """
    try:
        # 将集合转为列表并按字母排序
        sorted_words = sorted(list(word_set))
        with open(filepath, 'w', encoding='utf-8') as f:
            # 写入时，每个单词后面跟一个换行符
            f.write('\n'.join(sorted_words) + '\n')
        print(f"✅ 成功写入文件: {filepath} ({len(sorted_words)} 个单词)")
    except Exception as e:
        print(f"写入文件 {filepath} 时发生错误: {e}")


def process_article_and_analyze_difference():
    """
    执行整个流程：词频统计、词形还原、写入已使用单词、对比并写入未用到的单词。
    """
    # ----------------------------------------------------
    # 任务 1: 词形还原并提取已使用的单词 (USED WORDS)
    # ----------------------------------------------------
    print(f"--- 1. 正在处理文章文件: {ARTICLE_PATH} ---")
    used_words_set: Set[str] = set()
    try:
        with open(ARTICLE_PATH, 'r', encoding='utf-8') as f:
            article_text = f.read()

        # 使用 spaCy 处理文本 (这是耗时最长的步骤，但无法显示内部进度)
        print("   -> 正在进行高级自然语言处理 (词形还原)... 请稍候。")
        doc = nlp(article_text)
        print("   -> 文本处理完成。开始提取和过滤单词...")

        # 设置进度条参数
        total_tokens = len(doc)
        token_count = 0
        # 每隔 5% 打印一次进度，或者至少每 1000 个 token 打印一次 (取两者中的较大值)
        update_interval = max(1000, total_tokens // 20)

        for token in doc:
            token_count += 1

            # 每隔一段时间或在结尾时更新进度
            if token_count % update_interval == 0 or token_count == total_tokens:
                percent = (token_count / total_tokens) * 100
                # 使用 \r 回到行首，实现单行刷新进度条效果
                print(f"\r   -> 过滤进度: {token_count}/{total_tokens} ({percent:.1f}%)", end="", flush=True)

            # 过滤和还原逻辑
            if token.is_alpha and not token.is_stop:
                # spaCy 的 .lemma_ 属性会返回单词的原形 (如 running -> run, cats -> cat)
                lemma = token.lemma_.lower()
                used_words_set.add(lemma)

    except FileNotFoundError:
        print(f"❌ 错误：文章文件 {ARTICLE_PATH} 未找到。无法继续处理。")
        return

    # 确保进度条在循环结束后换行
    print("\n   -> 单词提取和过滤完成。")
    print(f"已从文章中提取出 {len(used_words_set)} 个独特的、还原后的单词。")

    # ----------------------------------------------------
    # 任务 2: 覆盖写入已使用的单词 (USED WORDS)
    # ----------------------------------------------------
    print(f"--- 2. 正在写入已使用的单词文件: {USED_WORDS_PATH} ---")
    write_words_from_set(USED_WORDS_PATH, used_words_set)

    # ----------------------------------------------------
    # 任务 3: 对比并提取未用到的单词 (UNUSED WORDS)
    # ----------------------------------------------------
    print(f"--- 3. 正在读取并对比单词表: {ALL_WORDS_PATH} ---")

    # 读取所有单词列表，并进行小写处理 (用于不区分大小写的对比)
    all_words_set = read_words_to_set(ALL_WORDS_PATH)
    print(f"从单词表文件中读取了 {len(all_words_set)} 个单词。")

    # 计算差集：所有单词 - 已使用的单词 = 未用到的单词
    # 注意：两个集合都已转为小写，保证了不区分大小写的对比
    unused_words_set = all_words_set - used_words_set

    print(f"找到 {len(unused_words_set)} 个未在文章中使用的单词。")

    # ----------------------------------------------------
    # 任务 4: 写入未用到的单词 (UNUSED WORDS)
    # ----------------------------------------------------
    print(f"--- 4. 正在写入未用到的单词文件: {UNUSED_WORDS_PATH} ---")
    write_words_from_set(UNUSED_WORDS_PATH, unused_words_set)

    print("\n🎉 所有任务完成！")
    print(f"结果已保存在 {UNUSED_WORDS_PATH}。")


if __name__ == "__main__":
    process_article_and_analyze_difference()

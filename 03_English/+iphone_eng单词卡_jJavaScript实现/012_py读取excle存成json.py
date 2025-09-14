
# 这个excel文件中,存放的是所有单词的内容

# 需要安装依赖库： pip install pandas openpyxl


import pandas as pd
import json
import os

# 定义Excel文件路径
excel_path = r"allword.xlsx"

# 读取Excel文件
df = pd.read_excel(
    excel_path,
    header=None,  # 无列标题
    usecols=[0, 1, 2, 3],  # 只读取A、B、C、D列
    names=["id", "词头", "释义和例句", "词根词缀"]  # 自定义列名
)

# 构建JSON数据结构
json_data = []
for _, row in df.iterrows():
    json_data.append({
        "id": str(row["id"]),  # 确保id为字符串类型
        "词头": row["词头"],
        "释义和例句": row["释义和例句"],
        "词根词缀": row["词根词缀"]
    })

# 生成JSON文件路径（与Excel同目录）
json_path = os.path.join(os.path.dirname(excel_path), "allword.json")

# 写入JSON文件
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"JSON文件已生成: {json_path}")




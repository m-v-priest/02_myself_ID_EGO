import random


def generate_math_problems(total_count=140):
    problems = set()
    ops = ['+', '-', '*', '/']

    # 计数器用于控制比例
    mul_count = 0
    div_count = 0
    target_mul_div = int(total_count * 0.33)

    def get_num(exclude_one=True):
        return random.randint(2 if exclude_one else 0, 99)

    def is_valid(res, expr):
        # 结果约束：不超过100，不等于1，且必须是整数
        if res <= 1 or res > 100 or int(res) != res:
            return False
        # 避免重复题目
        if expr in problems:
            return False
        return True

    while len(problems) < total_count:
        # 决定当前题目侧重哪种运算，以满足33%的比例
        if mul_count < target_mul_div:
            current_op_type = '*'
        elif div_count < target_mul_div:
            current_op_type = '/'
        else:
            current_op_type = random.choice(['+', '-'])

        expr = ""
        res = 0

        # 构造不同结构的题目
        structure = random.choice(['simple', 'compound', 'parens'])

        try:
            if structure == 'simple':  # a op b
                if current_op_type == '*':
                    # 避免 两位数 * 两位数
                    a, b = random.randint(2, 9), random.randint(2, 49)
                    if random.choice([True, False]): a, b = b, a
                    expr, res = f"{a}*{b}", a * b
                elif current_op_type == '/':
                    # 避免 两位数 / 两位数，且必须整除
                    b = random.randint(2, 9)
                    res_inner = random.randint(2, 50)
                    a = b * res_inner
                    if a > 99: continue
                    expr, res = f"{a}/{b}", res_inner
                else:
                    a, b = get_num(), get_num()
                    expr = f"{a}{current_op_type}{b}"
                    res = eval(expr)

            elif structure == 'compound':  # a op b op c
                # 随机生成带乘除的混合运算
                if current_op_type == '*':
                    a, b = random.randint(2, 9), random.randint(2, 10)
                    c = random.randint(2, 50)
                    op2 = random.choice(['+', '-'])
                    expr = f"{a}*{b}{op2}{c}"
                elif current_op_type == '/':
                    b = random.randint(2, 9)
                    a = b * random.randint(2, 12)
                    c = random.randint(2, 50)
                    op2 = random.choice(['+', '-'])
                    expr = f"{a}/{b}{op2}{c}"
                else:
                    a, b, c = get_num(), get_num(), get_num()
                    expr = f"{a}{random.choice(['+', '-'])}{b}{random.choice(['+', '-'])}{c}"
                res = eval(expr)

            elif structure == 'parens':  # (a op b) op c
                if current_op_type == '/':
                    # 例如 (16-8)/4+17
                    b_inner = random.randint(2, 9)
                    res_div = random.randint(2, 10)
                    a_inner = b_inner * res_div
                    # 拆分 a_inner 为 x + y 或 x - y
                    x = random.randint(a_inner + 1, 99)
                    expr = f"({x}-{x - a_inner})/{b_inner}+{random.randint(2, 50)}"
                else:
                    a, b, c = random.randint(2, 20), random.randint(2, 20), random.randint(2, 20)
                    expr = f"({a}+{b})*{random.randint(2, 5)}"
                res = eval(expr)

            # 最终校验
            if is_valid(res, expr):
                problems.add(f"{expr}=")
                if '*' in expr: mul_count += 1
                if '/' in expr: div_count += 1
        except:
            continue

    # 输出为 Asciidoc 表格格式
    prob_list = list(problems)
    print('[cols="1,1,1,1,1,1,1,1,1,1", options="header"]')
    print("|===")
    for i in range(14):
        row = prob_list[i * 10: (i + 1) * 10]
        print("| " + " | ".join(row))
    print("|===")


if __name__ == "__main__":
    generate_math_problems()
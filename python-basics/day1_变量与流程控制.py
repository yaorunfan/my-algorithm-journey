"""
Day 1 · 变量、数据类型、字符串、条件判断、循环
对应廖雪峰教程：Python 基础 → 数据类型和变量 / 字符串和编码 / 条件判断 / 循环

怎么用这个文件：
  1. 先通读「示范」部分，逐行看注释，在终端运行它看输出
  2. 再往下做「作业」，每个函数体里把 TODO 换成你自己的代码
  3. 保存后重新运行，最后会打印你的得分
  4. 全部通过 = 今天过关

运行命令（在终端里，先 cd 到本文件所在目录）：
  python3.14 day1_变量与流程控制.py
"""

# ============================================================
# 一、示范：照着看，看懂就行，不用背
# ============================================================

print("=" * 50)
print("Day 1 示范开始")
print("=" * 50)

# --- 1. 变量与基本类型 ---------------------------------------
# Python 不用声明类型，赋值即创建变量
name = "润凡"          # str  字符串
age = 24               # int  整数
height = 1.75          # float 浮点数
is_student = True      # bool 布尔值（注意 True/False 首字母大写）
nothing = None         # NoneType 空值

print("姓名:", name, type(name))
print("年龄:", age, type(age))

# --- 2. 算术运算 ---------------------------------------------
a, b = 7, 2
print(f"{a} + {b} = {a + b}")      # 加
print(f"{a} - {b} = {a - b}")      # 减
print(f"{a} * {b} = {a * b}")      # 乘
print(f"{a} / {b} = {a / b}")      # 除：结果一定是 float
print(f"{a} // {b} = {a // b}")    # 整除：只要整数部分（向下取整）
print(f"{a} % {b} = {a % b}")      # 取余
print(f"{a} ** {b} = {a ** b}")    # 幂

# --- 3. 字符串常用操作 ---------------------------------------
s = "  Hello, Python  "
print(f"原串: {s!r}")   #!r 会给字符串加上单引号显示
print(f"去空格: {s.strip()!r}") #.strip() = 把字符串两头的空格去掉（中间的不动）
print(f"转小写: {s.strip().lower()!r}")
print(f"长度: {len(s)}")
print(f"切割: {'a,b,c'.split(',')}") #按逗号切开，返回列表，不是字符串了
print(f"替换: {'hello'.replace('l', 'L')}")

# 索引从 0 开始，-1 表示最后一个
word = "Python"
print(f"第 1 个字符: {word[0]}")
print(f"最后 1 个字符: {word[-1]}")
print(f"前 3 个字符 word[0:3]: {word[0:3]}")   # 切片：左闭右开，不包含下标 3

# f-string：字符串前面加 f，用 {} 嵌入变量，最常用
print(f"我叫 {name}，今年 {age} 岁，身高 {height} 米")

# --- 4. 类型转换 ---------------------------------------------
print(f"int('42') = {int('42')}")          # 字符串 → 整数
print(f"float('3.14') = {float('3.14')}")  # 字符串 → 浮点
print(f"str(100) = {str(100)!r}")          # 数字 → 字符串
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 四舍五入保留 2 位小数

# --- 5. 条件判断 ---------------------------------------------
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# --- 6. 循环 -------------------------------------------------
# for 循环：遍历一个序列
total = 0
for i in range(1, 101):   # range(1, 101) 产生 1,2,3,...,100（左闭右开）
    total += i
print(f"1 到 100 的和 = {total}")

# while 循环：条件为真就一直转
n = 1
while n <= 5:
    print(f"  while 第 {n} 次", end="") #end是印完这一行，打印空的符号，不默认换行。
    n += 1
print() #打印换行符

# break 提前跳出，continue 跳过本次
for i in range(1, 11):
    if i == 3:
        continue        # 跳过 3
    if i == 7:
        break           # 到 7 就整个结束
    print(f"  循环体 i={i}", end="")

print()
print("=" * 50)
print("Day 1 示范结束，下面开始做作业")
print("=" * 50)


# ============================================================
# 二、作业：把每个 TODO 换成你的代码
# ============================================================

def f1_bmi(weight_kg, height_m):
    """计算 BMI = 体重 / 身高²，结果保留 2 位小数。

    例：f1_bmi(70, 1.75) 应返回 22.86
    提示：用 round(值, 2)
    """
    # TODO: 在这里写你的代码，并 return 结果
    BMI = weight_kg/(height_m ** 2)
    
    return round(BMI , 2)


def f2_grade(score):
    """按分数返回等级字符串。

    >= 90 -> "优秀"
    >= 80 -> "良好"
    >= 60 -> "及格"
    其余  -> "不及格"
    """
    # TODO
    if score >= 90:
        grade = '优秀'
    elif score >= 80:
        grade = '良好'
    elif score >= 60:
        grade = '及格'
    else:
        grade = '不及格'
    return grade


def f3_sum_even(n):
    """返回 1 到 n（含 n）之间所有偶数的和。

    例：f3_sum_even(10) = 2+4+6+8+10 = 30
    提示：用 for 循环 + if 判断，或者用 range 的步长 range(2, n+1, 2)
    """
    # TODO
    sum_even = 0
    for i in range(1 , n+1):
        if i % 2 == 0:
            sum_even = sum_even + i
    return sum_even


def f4_count_vowels(s):
    """返回字符串 s 中元音字母 (a e i o u) 的个数，不分大小写。

    例：f4_count_vowels("Hello World") = 3   # e, o, o
    提示：先把 s 转成小写，再逐个字符判断 in "aeiou"
    """
    # TODO
    word = s.lower()
    count = 0
    for ch in word:
        if ch in 'aeiou':
            count = count + 1
    return count


def f5_reverse_str(s):
    """返回 s 的反转字符串。

    例：f5_reverse_str("abcde") = "edcba"
    提示：切片写法 s[::-1]，-1 表示倒着取
    """
    # TODO
    reverse = s[::-1]
    return reverse


# ============================================================
# 三、自动判分：不用改下面任何一行，直接运行看结果
# ============================================================

_PASS = 0
_TOTAL = 0


def check(name, got, want):
    global _PASS, _TOTAL
    _TOTAL += 1
    if got == want:
        _PASS += 1
        print(f"  ✅ {name}")
    else:
        print(f"  ❌ {name}")
        print(f"     你的结果: {got!r}")
        print(f"     期望结果: {want!r}")


if __name__ == "__main__":
    print()
    print("---- Day 1 作业判分 ----")

    check("f1_bmi(70, 1.75)", f1_bmi(70, 1.75), 22.86)
    check("f1_bmi(50, 1.60)", f1_bmi(50, 1.60), 19.53)

    check("f2_grade(95)", f2_grade(95), "优秀")
    check("f2_grade(80)", f2_grade(80), "良好")
    check("f2_grade(59)", f2_grade(59), "不及格")

    check("f3_sum_even(10)", f3_sum_even(10), 30)
    check("f3_sum_even(1)", f3_sum_even(1), 0)

    check("f4_count_vowels('Hello World')", f4_count_vowels("Hello World"), 3)
    check("f4_count_vowels('xyz')", f4_count_vowels("xyz"), 0)

    check("f5_reverse_str('abcde')", f5_reverse_str("abcde"), "edcba")

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 1 全部通过！可以开始 Day 2 了")
    else:
        print("继续加油，把 ❌ 的改到通过为止。")


# ============================================================
# 四、参考答案（强烈建议先自己写，实在卡住再看）
# ============================================================
_参考答案 = r'''
def f1_bmi(weight_kg, height_m):
    return round(weight_kg / height_m ** 2, 2)

def f2_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

def f3_sum_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

def f4_count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def f5_reverse_str(s):
    return s[::-1]
'''
# 想看答案就把下一行的注释去掉，然后运行：
# print(_参考答案)

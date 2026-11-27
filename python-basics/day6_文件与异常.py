"""
Day 6 · 文件读写、JSON、异常处理
对应廖雪峰教程：错误、调试和测试 → 错误处理 ／ IO 编程 → 文件读写 / 操作文件和目录

今天的目标：让程序能「存东西、读东西」，并且在出错时不直接崩溃。
这两件事是后面所有自动化脚本和数据处理的地基。

运行命令：
  python3.14 day6_文件与异常.py
"""

import json
import tempfile
import shutil
from pathlib import Path

# ============================================================
# 一、示范
# ============================================================

print("=" * 50)
print("Day 6 示范开始")
print("=" * 50)

# 建一个临时目录来做实验，不污染你的桌面
work = Path(tempfile.mkdtemp(prefix="day6_"))
print(f"实验目录: {work}")

# --- 1. 写文件：永远用 with + 指定 encoding -------------------
p = work / "hello.txt"        # 用 / 拼路径，比字符串拼接安全
with open(p, "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
print(f"写好了: {p}")
# print(p.read_text(encoding="utf-8")) 输出可看到写进去的内容

# --- 2. 读文件 -------------------------------------------------
# 方式一：一次性读出全部内容
with open(p, "r", encoding="utf-8") as f:
    content = f.read()
print(f"read() 读到: {content!r}") #!r 表示用 repr 形式打印——也就是给字符串加上引号，并把 \n 显示成字面的 \n 而不是真的换行。

# 方式二：按行读（大文件必须这样，内存才不会爆）——最常用
with open(p, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"  第 {i} 行: {line.rstrip()}")   # rstrip() 去掉行尾的 \n，因为print自带换行，不去掉一个、n就会多一个换行

# 方式三：读成列表
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"readlines() 得到 {len(lines)} 行")

# ⚠️ 三个必记点：
#   1) 必须写 encoding="utf-8"，否则中文在别的系统上会乱码
#   2) "w" 会清空原文件！想追加用 "a"
#   3) 一定要用 with，它会在结束时自动关闭文件

# --- 3. JSON：结构化数据存盘的标准格式 -------------------------
data = {"name": "润凡", "scores": [90, 85, 88], "active": True}
jp = work / "data.json"

with open(jp, "w", encoding="utf-8") as f: # w指的是若文件不存在，则新建，若文件存在，则清空重写。
    # ensure_ascii=False 才能让中文按原样存，而不是 \uXXXX
    json.dump(data, f, ensure_ascii=False, indent=2) #false是让中文原样输出，而不是输出成ascii码形式。ident=2是每层缩进两个空格。
#dump：Python 对象 → JSON 文本 → 写到磁盘，文件内容确实是人可读的文本。
with open(jp, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"JSON 读回: {loaded}")
print(f"类型仍是 dict: {type(loaded)}")
#load：磁盘上的 JSON 文本 → 还原成 Python 对象 → 回到内存。

# --- 4. 异常处理：出错不要让它崩 -------------------------------
# 先看看不处理会怎样（这只是演示，故意触发）
try:                           #try: 里的代码「出事了就跳到 except」，没事就跳过 except。
    x = 10 / 0
except ZeroDivisionError as e: #把异常对象存到变量e，方便看细节
    print(f"被捕获了: {type(e).__name__} - {e}")

# 读一个不存在的文件
try:
    with open(work / "不存在的文件.txt", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as e:
    print(f"被捕获了: {type(e).__name__}")

# 转换失败
try:
    n = int("abc")
except ValueError as e:
    print(f"被捕获了: {type(e).__name__}: {e}")

# 完整的 try / except / else / finally
def safe_parse(text):
    try:
        value = int(text)
    except ValueError:
        print(f"  {text!r} 不是合法整数，返回 None")
        return None
    else:
        print(f"  {text!r} 解析成功 -> {value}")
        return value
    finally:
        # 不管成功失败都会执行，适合放清理代码
        print("  （finally 一定执行）")

print("safe_parse 演示:")
safe_parse("42")
safe_parse("abc")

# --- 5. 主动抛出异常 + 自定义异常 ------------------------------
class ScoreError(Exception):
    """自定义异常：继承 Exception 就行"""

def check_score(score):
    if not 0 <= score <= 100:
        raise ScoreError(f"分数必须在 0-100 之间，你给了 {score}")
    return score

try:
    check_score(120)
except ScoreError as e:
    print(f"被捕获了: {e}")

# --- 6. 操作目录 ----------------------------------------------
sub = work / "子目录"
sub.mkdir(exist_ok=True)                     # exist_ok=True：已存在也不报错
(sub / "a.txt").write_text("内容", encoding="utf-8")   # pathlib 的便捷写法
print(f"子目录存在? {sub.is_dir()}")
print(f"列出内容: {[f.name for f in work.iterdir()]}")
print(f"这个文件是文件吗? {(work / 'hello.txt').is_file()}")

# --- 7. 常见异常类型速查 --------------------------------------
常见异常 = {
    "ZeroDivisionError": "除以 0",
    "ValueError": "类型对但值不对，如 int('abc')",
    "TypeError": "类型不对，如 1 + 'a'",
    "KeyError": "字典里没有这个键",
    "IndexError": "列表下标越界",
    "FileNotFoundError": "文件不存在",
    "AttributeError": "对象没有这个属性/方法",
}
for k, v in 常见异常.items():
    print(f"  {k:22s} {v}")

print("=" * 50)
print("Day 6 示范结束")
print("=" * 50)


# ============================================================
# 二、作业
# ============================================================

def f1_count_lines(path):
    """返回文本文件的行数。

    例：一个内容是 "a\\nb\\nc\\n" 的文件 -> 3 行；空文件 -> 0
    提示：用 with open(..., encoding="utf-8") 按行遍历，每读一行计数 +1。
          注意别把最后一行之外的东西算进去。
    """
    # TODO
    count = 0
    with open(path , "r" , encoding="utf-8") as f:
        for _ in f:
            count = count + 1
    return count


def f2_write_read_json(path, data):
    """把 data 以 JSON 写入 path，再读回来并返回读回的对象。

    例：f2_write_read_json(p, {"a": 1}) -> {"a": 1}
    提示：写的时候用 json.dump(data, f, ensure_ascii=False)，
          读的时候用 json.load(f)。两个都要配 with open。
    """
    # TODO
    with open(path , "w" , encoding="utf-8") as f:
        json.dump(data , f , ensure_ascii=False)
    with open(path , "r" , encoding="utf-8") as f:
        loaded = json.load(f)
    return loaded


def f3_safe_div(a, b):
    """安全除法：能算就返回结果，除以 0 就返回 None（不要让它报错）。

    例：f3_safe_div(10, 2) -> 5.0
        f3_safe_div(1, 0)  -> None
    提示：try / except ZeroDivisionError
    """
    # TODO
    try:
        return a / b
    except ZeroDivisionError:
        return None


def f4_sum_numbers_from_file(path):
    """把文件里每行的数字加起来返回。跳过空行和非数字的行，不要让程序崩溃。

    例：文件内容是 "1\\n2\\nabc\\n\\n3\\n" -> 返回 6
    提示：逐行 strip()，空行 continue；用 try/except ValueError 包住 int(line)，
          失败的 continue 跳过。
    """
    # TODO
    total = 0
    with open(path , "r" ,encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                total = total + int(line)
            except ValueError:
                continue
    return total


def f5_make_dir(path):
    """创建目录（包括缺失的父目录），返回对应的 Path 对象。已存在时也不报错。

    例：f5_make_dir(某路径).is_dir() -> True
    提示：p = Path(path); p.mkdir(parents=True, exist_ok=True); return p
    """
    # TODO
    p = Path(path)
    p.mkdir(parents = True , exist_ok= True)
    return p


# ============================================================
# 三、自动判分
# ============================================================

_PASS = 0
_TOTAL = 0


def safe(expr_fn):
    """把可能报错的表达式包起来执行。报错时返回一句提示，而不是让整个程序崩掉。"""
    try:
        return expr_fn()
    except Exception as e:
        return f"<报错：{type(e).__name__}>"


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
    print("---- Day 6 作业判分 ----")

    test_dir = Path(tempfile.mkdtemp(prefix="day6_test_"))

    # f1
    f_a = test_dir / "three.txt"
    f_a.write_text("a\nb\nc\n", encoding="utf-8")
    f_b = test_dir / "empty.txt"
    f_b.write_text("", encoding="utf-8")
    check("f1 三行文件", f1_count_lines(f_a), 3)
    check("f1 空文件", f1_count_lines(f_b), 0)

    # f2
    f_c = test_dir / "out.json"
    check("f2 写入并读回", f2_write_read_json(f_c, {"name": "润凡", "n": 3}),
          {"name": "润凡", "n": 3})
    check("f2 文件确实存在", f_c.is_file(), True)

    # f3
    check("f3 正常除法", f3_safe_div(10, 2), 5.0)
    check("f3 除零返回 None", f3_safe_div(1, 0), None)

    # f4
    f_d = test_dir / "nums.txt"
    f_d.write_text("1\n2\nabc\n\n3\n", encoding="utf-8")
    check("f4 求和跳过非法行", f4_sum_numbers_from_file(f_d), 6)

    # f5
    deep = test_dir / "x" / "y" / "z"
    check("f5 创建嵌套目录", safe(lambda: f5_make_dir(deep).is_dir()), True)
    check("f5 重复创建不报错", safe(lambda: f5_make_dir(deep).is_dir()), True)

    shutil.rmtree(test_dir, ignore_errors=True)

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 6 全部通过！")
    else:
        print("把 ❌ 的改到通过为止，再进入 Day 7。")


# ============================================================
# 四、参考答案
# ============================================================
_参考答案 = r'''
def f1_count_lines(path):
    count = 0
    with open(path, "r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    return count


def f2_write_read_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def f3_safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def f4_sum_numbers_from_file(path):
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                total += int(line)
            except ValueError:
                continue
    return total


def f5_make_dir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
'''
# print(_参考答案)

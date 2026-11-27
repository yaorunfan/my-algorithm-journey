"""
Day 7 · 综合项目：成绩分析器 + 模块 / 虚拟环境
对应廖雪峰教程：模块 → 使用模块 / 安装第三方模块 ／ 错误调试测试 → 单元测试

今天的目标：把前 6 天学的东西串成一个真正有用的小工具。
做完这个，你就「能独立写出 100 行以上的脚本」了——这就是阶段一第 1 周期的验收标准之一。

运行命令：
  python3.14 day7_综合项目.py
"""

from pathlib import Path
import tempfile
import shutil

# ============================================================
# 一、示范
# ============================================================

print("=" * 50)
print("Day 7 示范开始")
print("=" * 50)

# --- 1. 导入模块：站在标准库的肩膀上 ---------------------------
import statistics                 # 统计模块
from collections import Counter   # 计数器
from datetime import date         # 日期

print(f"statistics.mean([1,2,3,4]) = {statistics.mean([1, 2, 3, 4])}")
print(f"statistics.median([1,2,3,4]) = {statistics.median([1, 2, 3, 4])}")
print(f"statistics.stdev([2,4,4,4,5,5,7,9]) = {statistics.stdev([2, 4, 4, 4, 5, 5, 7, 9]):.4f}")

words = "a b a c a b".split() #按空格切分成列表['a','b','a','c','a','b']
print(f"Counter 计数: {Counter(words)}")
print(f"出现最多的 2 个: {Counter(words).most_common(2)}")

print(f"今天日期: {date.today()}")

# --- 2. __name__ == "__main__" 是什么 -------------------------
# 这个文件被「直接运行」时，__name__ 等于 "__main__"，下面的代码才执行；
# 被「import 到别的文件」时，__name__ 等于文件名，下面的代码不执行。
# 作用：让文件既能当脚本跑，又能当模块被复用。
print(f"当前 __name__ = {__name__!r}")

# --- 3. 自测：把「对答案」这件事也自动化 -----------------------
def add(a, b):
    return a + b

# 一个最小可用的单元测试思路：用 assert 断言，错了就当场报错
assert add(1, 2) == 3
assert add(-1, 1) == 0
print("add() 的两个断言都通过 ✅")

# 专业的写法用 unittest 或 pytest。等你要写第一个正式项目时再学，
# 今天只要记住这个原则：写完函数，立刻用几组数据（含边界值）验一遍。

print("=" * 50)
print("Day 7 示范结束")
print("=" * 50)


# ============================================================
# 二、作业：把这五个函数连起来，就是一个完整的成绩分析器
# ============================================================

def f1_parse_scores(text):
    """解析多行文本，每行格式是 "姓名,分数"，返回 {姓名: [分数, ...]}。

    例：f1_parse_scores("小明,88\\n小红,95\\n小明,80\\n")
        -> {"小明": [88, 80], "小红": [95]}
    要求：忽略空行；分数转成 int。
    提示：用 split(",") 拆开，用 setdefault(name, []).append(score)
    """
    # TODO
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts)!=2:
            continue
        name = parts[0].strip()
        try:
            score = int(parts[1].strip())
        except ValueError:
            continue
        result.setdefault(name , []).append(score)
    return result


def f2_stats(scores):
    """对一组分数做统计，返回字典：
        {"count": 人数, "average": 平均分(保留1位小数),
         "max": 最高分, "min": 最低分, "pass_rate": 及格率百分比(保留1位小数)}

    例：f2_stats([80, 90, 60, 30])
        -> {"count": 4, "average": 65.0, "max": 90, "min": 30, "pass_rate": 75.0}
    及格定义：>= 60。及格率是百分数，即 (及格人数 / 总人数) * 100。
    提示：空列表要单独处理，返回 count=0 且其余为 0。
    """
    # TODO
    if not scores:
        return {"count" : 0,"average" : 0,"max" : 0,"min" : 0,"pass_rate" : 0}
    n = len(scores)
    passed = sum(1 for s in scores if s>=60)
    return {"count" : n,"average" : round(sum(scores)/n , 1),"max" : max(scores),"min" : min(scores),"pass_rate" : round((passed/n)*100 , 1)}


def f3_write_report(path, stats):
    """把 stats 写成一份人类可读的文本报告，写入 path，并返回写入的字符串。

    例：报告里应当包含 "平均分"、"最高分"、"及格率" 这几个词。
    提示：用 f-string 拼多行字符串，最后 with open(path, "w", encoding="utf-8") 写进去。
    """
    # TODO
    text = ("=====成绩分析报告=====\n"
            f"人数:{stats['count']}\n"
            f"平均分:{stats['average']}\n"
            f"最高分:{stats['max']}\n"
            f"最低分:{stats['min']}\n"
            f"及格率:{stats['pass_rate']}%\n")
    with open(path, "w" , encoding="utf-8")as f:
        f.write(text)
    return text


def f4_load_scores(path):
    """从文件读取成绩，返回 {姓名: [分数, ...]}。
    跳过无法解析的行（分隔符不对、分数不是数字等），不要让程序崩溃。

    例：文件内容 "小明,88\\n坏行\\n小红,abc\\n小明,80\\n"
        -> {"小明": [88, 80]}
    提示：读文件后用 f1 的同款逻辑解析每行，用 try/except 兜住 int() 的失败。
    """
    # TODO
    result = {}
    with open(path , "r" , encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts)!=2 :
                continue
            name = parts[0].strip()
            try:
                score = int(parts[1].strip())
            except ValueError:
                continue
            result.setdefault(name , []).append(score)
    return result


def f5_top_n(scores_by_name, n):
    """按总分从高到低排名，返回前 n 名，格式 [(姓名, 总分), ...]。

    例：f5_top_n({"小明": [88, 80], "小红": [95], "小刚": [70, 75]}, 2)
        -> [("小明", 168), ("小刚", 145)]
    提示：先算每人总分，用 sorted(..., key=lambda kv: kv[1], reverse=True) 排序，
          再切片取前 n 个。如果 n 超过人数，就全部返回。
    """
    # TODO
    totals = []
    for name , scores in scores_by_name.items():
        totals.append((name , sum(scores)))
    totals.sort(key = lambda kv:kv[1],reverse=True)
    return totals[:n]


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
    print("---- Day 7 作业判分 ----")

    check("f1 解析文本",
          f1_parse_scores("小明,88\n小红,95\n小明,80\n"),
          {"小明": [88, 80], "小红": [95]})
    check("f1 忽略空行",
          f1_parse_scores("\n小明,88\n\n"),
          {"小明": [88]})

    check("f2 统计", f2_stats([80, 90, 60, 30]),
          {"count": 4, "average": 65.0, "max": 90, "min": 30, "pass_rate": 75.0})
    check("f2 空列表", f2_stats([]),
          {"count": 0, "average": 0, "max": 0, "min": 0, "pass_rate": 0})

    test_dir = Path(tempfile.mkdtemp(prefix="day7_"))
    rp = test_dir / "report.txt"
    report = f3_write_report(rp, f2_stats([80, 90]))
    check("f3 文件已生成", rp.is_file(), True)
    check("f3 报告含平均分", safe(lambda: "平均分" in report), True)
    check("f3 报告含及格率", safe(lambda: "及格率" in report), True)

    fp = test_dir / "scores.txt"
    fp.write_text("小明,88\n坏行\n小红,abc\n小明,80\n", encoding="utf-8")
    check("f4 跳过非法行", f4_load_scores(fp), {"小明": [88, 80]})

    check("f5 前 2 名",
          f5_top_n({"小明": [88, 80], "小红": [95], "小刚": [70, 75]}, 2),
          [("小明", 168), ("小刚", 145)])
    check("f5 n 超过人数",
          f5_top_n({"a": [1]}, 5),
          [("a", 1)])

    shutil.rmtree(test_dir, ignore_errors=True)

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 7 全部通过！")
        print()
        print("★ 阶段一第 1 周期 · Python 基础 已完成 ★")
        print("接下来：把 GitHub 仓库建起来，把这个项目传上去，然后开始刷代码随想录的数组专题。")
    else:
        print("把 ❌ 的改到通过为止。")


# ============================================================
# 四、参考答案
# ============================================================
_参考答案 = r'''
def f1_parse_scores(text):
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 2:
            continue
        name = parts[0].strip()
        try:
            score = int(parts[1].strip())
        except ValueError:
            continue
        result.setdefault(name, []).append(score)
    return result


def f2_stats(scores):
    if not scores:
        return {"count": 0, "average": 0, "max": 0, "min": 0, "pass_rate": 0}
    n = len(scores)
    passed = sum(1 for s in scores if s >= 60)
    return {
        "count": n,
        "average": round(sum(scores) / n, 1),
        "max": max(scores),
        "min": min(scores),
        "pass_rate": round(passed / n * 100, 1),
    }


def f3_write_report(path, stats):
    text = (
        "===== 成绩分析报告 =====\n"
        f"人数：{stats['count']}\n"
        f"平均分：{stats['average']}\n"
        f"最高分：{stats['max']}\n"
        f"最低分：{stats['min']}\n"
        f"及格率：{stats['pass_rate']}%\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


def f4_load_scores(path):
    result = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            name = parts[0].strip()
            try:
                score = int(parts[1].strip())
            except ValueError:
                continue          # 分数不是数字 -> 整行跳过，不留下空列表
            result.setdefault(name, []).append(score)
    return result


def f5_top_n(scores_by_name, n):
    totals = [(name, sum(scores)) for name, scores in scores_by_name.items()]
    totals.sort(key=lambda kv: kv[1], reverse=True)
    return totals[:n]
'''
# print(_参考答案)

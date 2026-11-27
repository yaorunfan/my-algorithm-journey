"""
Day 3 · 字典 dict 与集合 set
对应廖雪峰教程：Python 基础 → 使用 dict 和 set

今天的目标：掌握「用哈希表快速查找」这个思想。
刷题里最高频的一类题（两数之和、字母异位词、最长的连续序列）全靠它。

运行命令：
  python3.14 day3_字典与集合.py
"""

# ============================================================
# 一、示范
# ============================================================

print("=" * 50)
print("Day 3 示范开始")
print("=" * 50)

# --- 1. 创建字典：键 → 值 的映射 -----------------------------
person = {"name": "润凡", "age": 24, "city": "西安"}
print(f"person = {person}")

# --- 2. 取值 -------------------------------------------------
print(f"person['name'] = {person['name']}")
print(f"person.get('school') = {person.get('school')}")            # 键不存在返回 None，不报错
print(f"person.get('school', '未知') = {person.get('school', '未知')}")  # 如果前面的查不到，就输出“，”后面的结果。给个默认值
# print(person['school'])   # 取消注释会报 KeyError —— 这就是为什么要用 get

# --- 3. 增删改 -----------------------------------------------
person["school"] = "西交大"          # 键不存在 -> 新增
person["age"] = 25                   # 键存在   -> 覆盖
print(f"新增/修改后: {person}")
del person["city"]                   # 删除
print(f"删除 city 后: {person}")
print(f"'age' in person -> {'age' in person}")

# --- 4. 遍历 -------------------------------------------------
for k in person:                     # 默认遍历键
    print(f"  键: {k}", end="")
print()
for k, v in person.items():          # 同时拿键和值（最常用）
    print(f"  {k} = {v}", end="")
print()
print(f"  所有键: {list(person.keys())}")
print(f"  所有值: {list(person.values())}")

# --- 5. 计数：字典最经典的用法 ---------------------------------
text = "the quick brown fox jumps over the lazy dog the end"
counter = {} #建一个空字典
for w in text.split():
    counter[w] = counter.get(w, 0) + 1     # 没出现过就当 0，再加 1
print(f"词频: {counter}")
print(f"出现最多的词: {max(counter, key=counter.get)}（{max(counter.values())} 次）")

# --- 6. 字典推导式 -------------------------------------------
print(f"平方表: {{x: x**2 for x in range(1, 5)}} = "
      f"{{x: x ** 2 for x in range(1, 5)}}")
print(f"  实际计算: { {x: x ** 2 for x in range(1, 5)} }")

# --- 7. 集合 set：只存不重复的元素 ---------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}, b = {b}")
print(f"交集 a & b = {a & b}")
print(f"并集 a | b = {a | b}")
print(f"差集 a - b = {a - b}")
print(f"对称差 a ^ b = {a ^ b}")

# set 最快的用途：去重 和 判断存在
nums = [1, 1, 2, 3, 3, 3]
print(f"列表去重（不给顺序保证）: {list(set(nums))}")
print(f"3 in a -> {3 in a}")

# --- 8. 一个综合小例子：找出列表里第一个重复出现的元素 ---------
def first_duplicate(lst):
    seen = set()
    for x in lst:
        if x in seen:
            return x
        seen.add(x)
    return None

print(f"first_duplicate([1,3,4,3,2]) = {first_duplicate([1, 3, 4, 3, 2])}")

print("=" * 50)
print("Day 3 示范结束")
print("=" * 50)


# ============================================================
# 二、作业
# ============================================================

def f1_word_count(text):
    """统计 text 里每个单词出现的次数，返回字典。单词按空格切分，统一转小写。

    例：f1_word_count("a b A c B b") -> {"a": 2, "b": 3, "c": 1}
    提示：text.lower().split()，然后用 get(w, 0) + 1 累加
    """
    # TODO
    text = text.lower().split()
    counter = {}
    for w in text:
        counter[w] = counter.get(w,0) + 1
    return counter


def f2_two_sum(nums, target):
    """找出 nums 中和为 target 的两个数的下标，返回 [i, j]（i < j）。

    保证恰好有一组解。要求 O(n)，不能双重循环。
    例：f2_two_sum([2, 7, 11, 15], 9) -> [0, 1]
    提示：遍历时把「见过的值 -> 下标」存进字典，
          看 target - 当前值 是否在字典里
    """
    # TODO
    seen = {}
    for i , x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need],i]
        seen[x] = i
    return None


def f3_common(a, b):
    """返回两个列表的公共元素（去重 + 升序）。

    例：f3_common([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
    提示：sorted(set(a) & set(b))
    """
    # TODO
    return sorted(set(a) & set(b))


def f4_invert(d):
    """把字典的键和值互换，返回新字典。

    例：f4_invert({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    提示：字典推导式 {v: k for k, v in d.items()}
    """
    # TODO
    #return{v : k for k , v in d.items()} 这个是简洁写法
    
    result = {}
    for k , v in d.items():
        result[v] = k
    return result



def f5_group_by_len(words):
    """按单词长度分组，返回 {长度: [单词列表]}，同一组内保持原顺序。

    例：f5_group_by_len(["ab", "c", "de", "f"]) -> {2: ["ab", "de"], 1: ["c", "f"]}
    提示：遍历，用 setdefault(n, []).append(w)
          或者 if n not in d: d[n] = [] 然后 d[n].append(w)
    """
    # TODO
    d = {}
    for w in words:
        d.setdefault(len(w) , []).append(w)
    return d
    
    # d = {}
    # for w in words:
    #     n = len(w)
    #     if n not in d:
    #         d[n] = []
    #     d[n].append(w)
    # return d


# ============================================================
# 三、自动判分
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
    print("---- Day 3 作业判分 ----")

    check("f1 词频", f1_word_count("a b A c B b"), {"a": 2, "b": 3, "c": 1})
    check("f1 空串", f1_word_count(""), {})

    check("f2 两数之和", f2_two_sum([2, 7, 11, 15], 9), [0, 1])
    check("f2 相邻解", f2_two_sum([3, 2, 4], 6), [1, 2])

    check("f3 交集", f3_common([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
    check("f3 无交集", f3_common([1, 2], [3, 4]), [])

    check("f4 反转字典", f4_invert({"a": 1, "b": 2}), {1: "a", 2: "b"})

    check("f5 按长度分组", f5_group_by_len(["ab", "c", "de", "f"]),
          {2: ["ab", "de"], 1: ["c", "f"]})

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 3 全部通过！")
    else:
        print("把 ❌ 的改到通过为止，再进入 Day 4。")


# ============================================================
# 四、参考答案
# ============================================================
_参考答案 = r'''
def f1_word_count(text):
    d = {}
    for w in text.lower().split():
        d[w] = d.get(w, 0) + 1
    return d

def f2_two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return None

def f3_common(a, b):
    return sorted(set(a) & set(b))

def f4_invert(d):
    return {v: k for k, v in d.items()}

def f5_group_by_len(words):
    d = {}
    for w in words:
        d.setdefault(len(w), []).append(w)
    return d
'''
# print(_参考答案)

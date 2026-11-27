"""
Day 2 · 列表 list 与元组 tuple
对应廖雪峰教程：Python 基础 → 使用 list 和 tuple

今天的目标：把「一组数据」玩熟。刷题里 70% 的题都在操作列表。

运行命令：
  python3.14 day2_列表与元组.py
"""

# ============================================================
# 一、示范
# ============================================================

print("=" * 50)
print("Day 2 示范开始")
print("=" * 50)

# --- 1. 创建列表 ---------------------------------------------
nums = [3, 1, 4, 1, 5, 9, 2, 6]
words = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]      # 可以混放不同类型，但不建议
empty = []

print(f"nums = {nums}")

# --- 2. 索引与切片 -------------------------------------------
print(f"nums[0] = {nums[0]}")        # 第一个
print(f"nums[-1] = {nums[-1]}")      # 最后一个
print(f"nums[0:3] = {nums[0:3]}")    # 下标 0,1,2
print(f"nums[:3] = {nums[:3]}")      # 从头取到 3
print(f"nums[3:] = {nums[3:]}")      # 从 3 取到尾
print(f"nums[::2] = {nums[::2]}")    # 每隔一个取一个（步长 2）
print(f"nums[::-1] = {nums[::-1]}")  # 反过来

# --- 3. 增删改查 ---------------------------------------------
nums.append(100)                    # 尾部追加一个
print(f"append(100) 后: {nums}")
nums.insert(0, -1)                  # 在下标 0 插入
print(f"insert(0, -1) 后: {nums}")
nums.remove(-1)                     # 删除第一个值为 -1 的元素
print(f"remove(-1) 后: {nums}")
last = nums.pop()                   # 弹出并返回最后一个
print(f"pop() 返回 {last}，剩下 {nums}")
nums[0] = 999                       # 按下标修改
print(f"nums[0] = 999 后: {nums}")

# --- 4. 内置函数与统计 ---------------------------------------
print(f"len = {len(nums)}")
print(f"sum = {sum(nums)}")
print(f"max = {max(nums)}, min = {min(nums)}") 
print(f"排序 sorted() 返回新列表: {sorted(nums)}") #不改变原列表，生成一个新列表
print(f"原列表没变: {nums}")
print(f"原地排序 sort() 后: ", end="") 
nums.sort() #改变了原列表，没有新列表生成
print(nums)
print(f"降序: {sorted(nums, reverse=True)}")
print(f"按绝对值排序: {sorted([-3, 1, -2, 4], key=abs)}")

# --- 5. 判断与查找 -------------------------------------------
print(f"5 in nums -> {5 in nums}")
print(f"nums.index(5) -> {nums.index(5)}")   # 5 第一次出现的下标

# --- 6. 遍历的三种姿势 ---------------------------------------
for x in [10, 20, 30]:
    print(f"  取值: {x}", end="")

print()
for i, x in enumerate([10, 20, 30]):          # enumerate 同时拿到下标和值
    print(f"  下标 {i} 的值是 {x}", end="")

print()
names = ["润凡", "小明"]
scores = [95, 88]
for n, s in zip(names, scores):              # zip 把两个列表配对
    print(f"  {n}: {s} 分", end="")

print()
print("  带下标两两配对:", [f"{i}-{n}" for i, n in enumerate(names)])

# --- 7. 列表推导式（Python 最优雅的语法之一）-----------------
squares = [x ** 2 for x in range(1, 6)]  #左闭右开
print(f"平方列表: {squares}")
evens = [x for x in range(10) if x % 2 == 0]#从0开始
print(f"0-9 中的偶数: {evens}")

# --- 8. 元组 tuple：不可变的列表 -----------------------------
point = (3, 5)   #只要不修改，元组跟列表没区别
print(f"point = {point}, point[0] = {point[0]}")
# point[0] = 9   # 取消注释会报错 TypeError: 'tuple' object does not support item assignment
x, y = point                # 解包
print(f"解包: x = {x}, y = {y}")

print("=" * 50)
print("Day 2 示范结束")
print("=" * 50)


# ============================================================
# 二、作业
# ============================================================

def f1_dedup_keep_order(lst):
    """去掉重复元素，并保持第一次出现的顺序。

    例：f1_dedup_keep_order([3, 1, 3, 2, 1, 4]) -> [3, 1, 2, 4]
    提示：新建一个空列表 seen，遍历 lst，
          如果元素不在 seen 里就 append。（不要直接用 set，set 会打乱顺序）
    """
    # TODO
    seen = []
    for x in lst:
        if x not in seen:
            seen.append(x)  #append属于就地修改型，不能写成seen = seen.append(x)
    return seen


def f2_max_index(lst):
    """返回最大值第一次出现的下标。

    例：f2_max_index([1, 9, 3, 9]) -> 1
    提示：用 enumerate 遍历，记录当前最大值的下标
    """
    # TODO
    # for i , x in enumerate(lst):
    #     if x == max(lst):
    #         break
    # return i    #这种方法计算复杂度太高，每次循环都要计算一次max

    m = max(lst)
    for i , x in enumerate(lst):
        if x == m:
            break
    return i    #这种方法计算复杂度降低，循环内只比较，不计算
    #可以看下答案，答案的擂台方法更好一些
    #答案如下：
    # idx = 0
    # for i , x in enumerate(lst):
    #     if x > lst[idx]:
    #         idx = i
    # return idx



def f3_second_largest(lst):
    """返回列表中第二大的值（重复的不算）。

    例：f3_second_largest([5, 1, 9, 9, 3]) -> 5
    提示：先去重再排序，然后取倒数第二个
    """
    # TODO
    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)
    seen.sort()
    x = seen[-2]
    return x


def f4_rotate(lst, k):
    """把列表右移 k 位。

    例：f4_rotate([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    提示：用切片。新列表 = lst[-k:] + lst[:-k]
          注意 k 可能比列表长，可以先用 k = k % len(lst)
    """
    # TODO
    k = k % len(lst)
    seen = lst[-k:]
    for i in lst[:-k]:
        seen.append(i)
    return seen


def f5_chunk(lst, n):
    """把列表每 n 个一组切开，返回二维列表。

    例：f5_chunk([1,2,3,4,5,6,7], 3) -> [[1, 2, 3], [4, 5, 6], [7]]
    提示：用 for 循环 + 切片 lst[i:i+n]，range 的步长设为 n
    """
    # TODO
    seen = []
    k = len(lst)
    for i in range(0,k,n):
        seen = seen + [lst[i:i+n]]
        #或者写成
        #seen.append(lst[i:i+n])
    return seen


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
    print("---- Day 2 作业判分 ----")

    check("f1 去重保序", f1_dedup_keep_order([3, 1, 3, 2, 1, 4]), [3, 1, 2, 4])
    check("f1 无重复", f1_dedup_keep_order([1, 2, 3]), [1, 2, 3])

    check("f2 最大值下标", f2_max_index([1, 9, 3, 9]), 1)
    check("f2 单元素", f2_max_index([7]), 0)

    check("f3 第二大", f3_second_largest([5, 1, 9, 9, 3]), 5)
    check("f3 负数和正数", f3_second_largest([-1, -5, -3]), -3)

    check("f4 右移 2 位", f4_rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
    check("f4 k 超过长度", f4_rotate([1, 2, 3], 4), [3, 1, 2])

    check("f5 分块", f5_chunk([1, 2, 3, 4, 5, 6, 7], 3), [[1, 2, 3], [4, 5, 6], [7]])
    check("f5 整除", f5_chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 2 全部通过！")
    else:
        print("把 ❌ 的改到通过为止，再进入 Day 3。")


# ============================================================
# 四、参考答案
# ============================================================
_参考答案 = r'''
def f1_dedup_keep_order(lst):
    seen = []
    for x in lst:
        if x not in seen:
            seen.append(x)
    return seen

def f2_max_index(lst):
    idx = 0
    for i, x in enumerate(lst):
        if x > lst[idx]:
            idx = i
    return idx

def f3_second_largest(lst):
    uniq = sorted(set(lst))
    return uniq[-2]

def f4_rotate(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst[:]

def f5_chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
'''
# print(_参考答案)

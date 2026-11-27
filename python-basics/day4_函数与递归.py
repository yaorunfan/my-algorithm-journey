"""
Day 4 · 函数、参数、递归、lambda
对应廖雪峰教程：函数 → 调用函数 / 定义函数 / 函数的参数 / 递归函数

今天的目标：把代码「打包成可复用的块」。这是从「写脚本」到「写程序」的分水岭。

顺便引入一个算法工程师的思维习惯：写完一个函数，问自己两件事——
  1. 它的输入有什么边界情况？（0、空、负数、重复值）
  2. 它的时间复杂度是多少？

运行命令：
  python3.14 day4_函数与递归.py
"""

# ============================================================
# 一、示范
# ============================================================

print("=" * 50)
print("Day 4 示范开始")
print("=" * 50)

# --- 1. 定义与调用 -------------------------------------------
def greet(name):
    """这是文档字符串（docstring）。写清楚函数干什么，别人才能用。"""
    return f"你好，{name}！"

print(greet("润凡"))

# 没有 return 的函数返回 None
def show(msg):
    print(f"  [提示] {msg}")

result = show("这条消息会被打印")
print(f"show() 的返回值是: {result}")

# --- 2. 默认参数 ---------------------------------------------
def power(base, exp=2):
    return base ** exp

print(f"power(3)    = {power(3)}")       # 用默认 exp=2
print(f"power(3, 3) = {power(3, 3)}")    # 覆盖默认值

# 默认参数不要用可变对象（列表/字典）！这是个经典大坑
def bad_append(x, lst=None):
    if lst is None:          # 正确写法：默认值用 None，函数内再创建
        lst = []
    lst.append(x)
    return lst

print(f"第一次: {bad_append(1)}")
print(f"第二次: {bad_append(2)}   （如果默认值写成 lst=[]，这里会变成 [1, 2]）")

# --- 3. 关键字参数与可变参数 ---------------------------------
def describe(name, age, city="西安"):
    return f"{name}，{age} 岁，在{city}"

print(describe("润凡", 24))                    # 位置参数
print(describe(city="北京", age=24, name="润凡"))  # 关键字参数，顺序可以乱

def total(*args):
    """*args 把所有位置参数收成一个元组"""
    return sum(args)

print(f"total(1, 2, 3, 4) = {total(1, 2, 3, 4)}")

def show_info(**kwargs):
    """**kwargs 把关键字参数收成一个字典"""
    return kwargs

print(f"show_info(a=1, b=2) = {show_info(a=1, b=2)}")

# --- 4. 返回多个值（其实是返回元组） -------------------------
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5])
print(f"min_max([3,1,4,1,5]) -> lo={lo}, hi={hi}")

# --- 5. 作用域：函数内部的变量外面看不见 ---------------------
g = 100                # 全局变量
def local_demo():
    g = 200            # 这是新建的局部变量，不影响外面的 g
    return g

print(f"函数内 g={local_demo()}，函数外 g={g}")

# --- 6. lambda + map / filter / sorted -----------------------
print(f"lambda 平方: {(lambda x: x ** 2)(5)}")
print(f"map 每个元素乘 2: {list(map(lambda x: x * 2, [1, 2, 3]))}")
print(f"filter 保留偶数:   {list(filter(lambda x: x % 2 == 0, range(10)))}")

students = [("小明", 88), ("小红", 95), ("小刚", 88)]
print(f"按分数降序: {sorted(students, key=lambda s: s[1], reverse=True)}") #从大到小
print(f"按名字升序: {sorted(students, key=lambda s: s[0])}")

# --- 7. 递归：函数自己调用自己 -------------------------------
def factorial(n):
    if n <= 1:            # 递归出口，必须有，否则无限递归
        return 1
    return n * factorial(n - 1)   # 递归关系

print(f"5! = {factorial(5)}")

def fib(n):
    """朴素递归版斐波那契：n=35 时就会慢得明显（约 10 秒）。
    原因：f(n) 重复计算了大量子问题，时间复杂度 O(2^n)。
    改进方向（明天之后可以自己试）：加一个字典做缓存（记忆化）。
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"fib(10) = {fib(10)}   # 注意：别在这里调 fib(35)，会卡住")

# --- 8. 一个带复杂度意识的例子：判断质数 ---------------------
# 朴素做法：试除 2 到 n-1，O(n)
# 优化做法：只需要试到 √n，因为若 n = a*b，则 a、b 中必有一个 ≤ √n —— O(√n)
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:      # 等价于 i <= √n，但不用引入浮点开方
        if n % i == 0:
            return False
        i += 1
    return True

print(f"质数判断: {[(n, is_prime(n)) for n in range(1, 20)]}")

print("=" * 50)
print("Day 4 示范结束")
print("=" * 50)


# ============================================================
# 二、作业
# ============================================================

def f1_is_prime(n):
    """判断 n 是否为质数。小于 2 的数都不是质数。

    例：f1_is_prime(2) -> True
        f1_is_prime(1) -> False
        f1_is_prime(17) -> True
        f1_is_prime(-7) -> False
    要求：用 √n 的优化写法（示范里最后那段可以照着改）
    """
    # TODO
    if n < 2:
        return False
    i = 2
    while i * i <=n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def f2_fib(n):
    """返回第 n 个斐波那契数，约定 F(0)=0, F(1)=1。

    例：f2_fib(0)=0, f2_fib(1)=1, f2_fib(10)=55
    要求：用循环写（不要用示范里的朴素递归，那个太慢）。
          循环版本的时间复杂度是 O(n)，空间 O(1)。
    提示：用 a, b = b, a + b 这种同时赋值的写法
    """
    # TODO
    a = 0
    b = 1
    for _ in range(n):
        a , b = b , a+b
    return a


def f3_factorial(n):
    """用递归计算 n!（n 的阶乘），约定 f3_factorial(0) = 1。

    例：f3_factorial(0)=1, f3_factorial(5)=120
    要求：必须是递归写法（函数内部调用自己）
    """
    # TODO
    if n <= 1:
        return 1
    return n * f3_factorial(n-1)


def f4_binary_search(lst, target):
    """在已升序排列的列表 lst 中查找 target，返回下标；找不到返回 -1。

    例：f4_binary_search([1, 3, 5, 7, 9], 5) -> 2
        f4_binary_search([1, 3, 5, 7, 9], 4) -> -1
        f4_binary_search([], 1) -> -1
    注意：前提是 lst 已经有序，这个条件必须由调用方保证。
    提示：维护 left / right 两个指针，每次取中间 mid = (left + right) // 2，
          比较 lst[mid] 与 target，缩小一半区间。循环条件是 left <= right
    """
    # TODO
    left , right = 0 , len(lst) - 1
    while left <=right:
        mid = (left + right)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def f5_sort_students(students):
    """students 是 [(姓名, 分数), ...] 形式的列表。
    返回排好序的新列表：分数从高到低；分数相同时按姓名升序。

    例：f5_sort_students([("小明", 88), ("小红", 95), ("小刚", 88)])
        -> [("小红", 95), ("小刚", 88), ("小明", 88)]
    注意：中文按「字符编码顺序」比较，不是按拼音。
          刚(U+521A) < 明(U+660E)，所以小刚排在小明前面。这正是我们要的确定性行为。
    提示：用 sorted(..., key=...)。
          想按多个字段排序：key=lambda s: (-s[1], s[0])
          —— 分数取负号就等于降序；名字保持升序不变
    """
    # TODO
    return sorted(students , key = lambda s : (-s[1] , s[0]))


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
    print("---- Day 4 作业判分 ----")

    check("f1 is_prime(2)", f1_is_prime(2), True)
    check("f1 is_prime(1)", f1_is_prime(1), False)
    check("f1 is_prime(17)", f1_is_prime(17), True)
    check("f1 is_prime(-7)", f1_is_prime(-7), False)
    check("f1 is_prime(100)", f1_is_prime(100), False)

    check("f2 fib(0)", f2_fib(0), 0)
    check("f2 fib(1)", f2_fib(1), 1)
    check("f2 fib(10)", f2_fib(10), 55)

    check("f3 factorial(0)", f3_factorial(0), 1)
    check("f3 factorial(5)", f3_factorial(5), 120)

    check("f4 找到 5", f4_binary_search([1, 3, 5, 7, 9], 5), 2)
    check("f4 找不到 4", f4_binary_search([1, 3, 5, 7, 9], 4), -1)
    check("f4 空列表", f4_binary_search([], 1), -1)

    check("f5 排序学生",
          f5_sort_students([("小明", 88), ("小红", 95), ("小刚", 88)]),
          [("小红", 95), ("小刚", 88), ("小明", 88)])

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 4 全部通过！函数这一关过了，后面就轻松了")
    else:
        print("把 ❌ 的改到通过为止，再进入 Day 5。")


# ============================================================
# 四、参考答案
# ============================================================
_参考答案 = r'''
def f1_is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def f2_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def f3_factorial(n):
    if n <= 1:
        return 1
    return n * f3_factorial(n - 1)

def f4_binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def f5_sort_students(students):
    return sorted(students, key=lambda s: (-s[1], s[0]))
'''
# print(_参考答案)

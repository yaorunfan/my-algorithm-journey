"""
Day 5 · 类与对象（面向对象入门）
对应廖雪峰教程：面向对象 → 类和实例 / 访问限制 / 继承和多态

今天的目标：会定义一个类、会创建对象、会调用方法、会写继承。
刷题里用得到的地方：LRU 缓存、并查集、设计题（用栈实现队列）都是「设计一个类」。

运行命令：
  python3.14 day5_类与对象.py
"""

# ============================================================
# 一、示范
# ============================================================

print("=" * 50)
print("Day 5 示范开始")
print("=" * 50)

# --- 1. 最简单的类 -------------------------------------------
class Dog:
    """类 = 模板；对象 = 用模板造出来的具体东西。"""

    # __init__ 是构造方法，创建对象时自动调用
    # self 代表「这个对象自己」，永远是第一个参数，调用时不用手动传
    def __init__(self, name, age):
        self.name = name      # 实例属性：每个对象各有一份
        self.age = age

    def bark(self):           # 实例方法
        return f"{self.name} 说：汪！"

    def birthday(self):       # 会修改对象自己的状态
        self.age += 1

    def __str__(self):        # 决定 print(对象) 时显示什么
        return f"Dog({self.name}, {self.age}岁)"


d1 = Dog("旺财", 3)
d2 = Dog("来福", 5)

print(f"d1.name = {d1.name}")
print(d1.bark())
d1.birthday()
print(f"过完生日: {d1}")
print(f"d2 不受影响: {d2}")

# --- 2. 类属性 vs 实例属性 -----------------------------------
class Cat:
    species = "猫科动物"        # 类属性：所有实例共享

    def __init__(self, name):
        self.name = name        # 实例属性：各自独立

c1, c2 = Cat("咪咪"), Cat("橘座")
print(f"c1.species = {c1.species}, c2.species = {c2.species}")

# --- 3. 访问限制：约定用下划线开头表示「内部用，别乱碰」------
class Wallet:
    def __init__(self, owner, amount):
        self.owner = owner
        self._amount = amount     # 单个下划线 = 约定俗成的「私有」

    def spend(self, cost):
        """对外只暴露方法，内部数据自己管好 —— 这叫封装。"""
        if cost > self._amount:
            return False           # 钱不够，拒绝，且不改变状态
        self._amount -= cost
        return True

    def get_amount(self):
        return self._amount

w = Wallet("润凡", 100)
print(f"花钱 30 成功? {w.spend(30)}，余额 {w.get_amount()}")
print(f"花钱 200 成功? {w.spend(200)}，余额 {w.get_amount()}")

# --- 4. 继承 -------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "……"

    def intro(self):
        return f"我是 {self.name}，{self.speak()}"


class Pig(Animal):               # Pig 继承 Animal，自动获得 name 属性和 intro 方法
    def speak(self):             # 覆盖（override）父类的方法
        return "哼哼"


class Duck(Animal):
    def __init__(self, name, color):    # 子类想加属性，就得自己写 __init__
        super().__init__(name)          # 先让父类把自己那部分初始化好
        self.color = color

    def speak(self):
        return "嘎嘎"


for a in [Animal("神秘生物"), Pig("佩奇"), Duck("唐老鸭", "白")]:
    print(f"  {a.intro()}")       # 同一个 intro()，行为随对象而变 —— 多态

print("=" * 50)
print("Day 5 示范结束")
print("=" * 50)


# ============================================================
# 二、作业
# ============================================================

class Stack:
    """用列表实现一个「后进先出」的栈。

    需要提供这些方法：
      push(x)     —— 把 x 压入栈顶
      pop()       —— 弹出并返回栈顶元素；如果栈为空，返回 None
      peek()      —— 只返回栈顶元素，不弹出；空栈返回 None
      is_empty()  —— 栈为空返回 True，否则 False
      __len__()   —— 让 len(栈对象) 能工作，返回元素个数

    提示：内部用一个 self._items = [] 存数据。
          列表的 append / pop 天然就是栈的操作。
    """

    def __init__(self):
        # TODO: 初始化内部列表
        self._items = []

    def push(self, x):
        # TODO
        self._items.append(x)

    def pop(self):
        # TODO
        if self._items == []:
            return None
        return self._items.pop()

    def peek(self):
        # TODO
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self):
        # TODO
        if self._items:
            return False
        else:
            return True

    def __len__(self):
        # TODO
        return len(self._items)


class Student:
    """学生对象。

    要求：
      __init__(self, name, scores)  —— scores 是一个分数列表，默认给 None 表示空
      add_score(self, score)        —— 追加一个分数
      average(self)                 —— 返回平均分（保留 2 位小数）；没有成绩时返回 0.0
      best(self)                    —— 返回最高分；没有成绩时返回 0
      __str__(self)                 —— 返回 "姓名(平均分)"
    """

    def __init__(self, name, scores=None):
        # TODO
        self.name = name
        self.scores = list(scores) if scores else []

    def add_score(self, score):
        # TODO
        self.scores.append(score)

    def average(self):
        # TODO
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores),2) #round是四舍五入的意思round（数值，保留几位小数）

    def best(self):
        # TODO
        if not self.scores:
            return 0
        return max(self.scores)

    def __str__(self):
        # TODO
        return f"{self.name}({self.average()})"


class Rectangle:
    """矩形。

    要求：
      __init__(self, width, height)
      area(self)       —— 面积
      perimeter(self)  —— 周长
      is_square(self)  —— 是正方形返回 True
      __str__(self)    —— 返回 "Rectangle(3x4)" 这种格式
    """

    def __init__(self, width, height):
        # TODO
        self.width = width
        self.height = height

    def area(self):
        # TODO
        return self.width * self.height

    def perimeter(self):
        # TODO
        return 2 * (self.width + self.height)

    def is_square(self):
        # TODO
        if self.width == self.height:
            return True 
        else:
            return False
    
    def __str__(self):
        # TODO
        return f"Rectangle({self.width}x{self.height})"


class BankAccount:
    """银行账户。

    要求：
      __init__(self, balance=0)  —— 初始余额，属性名叫 self.balance
      deposit(self, amount)      —— 存钱，返回新余额
      withdraw(self, amount)     —— 取钱：够就扣掉并返回 True；
                                    余额不足返回 False，且余额不变
    """

    def __init__(self, balance=0):
        # TODO
        self.balance = balance

    def deposit(self, amount):
        # TODO
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        # TODO
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True


def f5_apply_twice(func, x):
    """把函数 func 连续作用两次：返回 func(func(x))。

    例：f5_apply_twice(lambda v: v + 3, 10) -> 16
    说明：函数可以当参数传递，也可以当返回值 —— 这叫「高阶函数」，
          是 Python 里非常常用的写法（sorted 的 key 就是这么用的）。
    """
    # TODO
    return func(func(x))


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
    print("---- Day 5 作业判分 ----")

    # --- Stack ---
    s = Stack()
    check("Stack 初识为空", s.is_empty(), True)
    check("Stack len=0", safe(lambda: len(s)), 0)
    s.push(1)
    s.push(2)
    check("push 两个后 len=2", safe(lambda: len(s)), 2)
    check("peek 不弹出", s.peek(), 2)
    check("peek 后 len 仍为 2", safe(lambda: len(s)), 2)
    check("pop 栈顶", s.pop(), 2)
    check("pop 后 len=1", safe(lambda: len(s)), 1)
    check("再 pop", s.pop(), 1)
    check("空栈 pop 返回 None", s.pop(), None)
    s.push(9)
    check("清空后再 push", s.peek(), 9)

    # --- Student ---
    st = Student("小明", [80, 90, 100])
    check("average", st.average(), 90.0)
    check("best", st.best(), 100)
    check("str", safe(lambda: str(st)), "小明(90.0)")
    st.add_score(70)
    check("add_score 后 average", st.average(), 85.0)
    st2 = Student("小红")
    check("无成绩 average", st2.average(), 0.0)
    check("无成绩 best", st2.best(), 0)

    # --- Rectangle ---
    r = Rectangle(3, 4)
    check("面积", r.area(), 12)
    check("周长", r.perimeter(), 14)
    check("不是正方形", r.is_square(), False)
    check("str", safe(lambda: str(r)), "Rectangle(3x4)")
    check("正方形判断", Rectangle(5, 5).is_square(), True)

    # --- BankAccount ---
    acc = BankAccount()
    check("初始余额", safe(lambda: acc.balance), 0)
    check("存款返回新余额", acc.deposit(100), 100)
    check("取款成功", acc.withdraw(30), True)
    check("取款后余额", safe(lambda: acc.balance), 70)
    check("取款失败", acc.withdraw(1000), False)
    check("失败后余额不变", safe(lambda: acc.balance), 70)

    # --- 高阶函数 ---
    check("apply_twice +3", f5_apply_twice(lambda v: v + 3, 10), 16)

    print()
    print(f"得分：{_PASS} / {_TOTAL}")
    if _PASS == _TOTAL:
        print("🎉 Day 5 全部通过！")
    else:
        print("把 ❌ 的改到通过为止，再进入 Day 6。")


# ============================================================
# 四、参考答案
# ============================================================
_参考答案 = r'''
class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if not self._items:
            return None
        return self._items.pop()

    def peek(self):
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


class Student:
    def __init__(self, name, scores=None):
        self.name = name
        self.scores = list(scores) if scores else []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores), 2)

    def best(self):
        return max(self.scores) if self.scores else 0

    def __str__(self):
        return f"{self.name}({self.average()})"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


def f5_apply_twice(func, x):
    return func(func(x))
'''
# print(_参考答案)

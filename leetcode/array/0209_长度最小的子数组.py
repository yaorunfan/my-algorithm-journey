# 209. 长度最小的子数组 | 数组 | 难度：中等
# 思路：滑动窗口。right 指针扩张累加，一旦 sum >= target，
#       left 指针收缩、同时更新最短长度，直到 sum 重新 < target。
# 时间复杂度 O(n)（每个元素最多被 left、right 各扫过一次）｜空间复杂度 O(1)
#
# 踩坑记录：
# 1. min_len 用 float('inf') 当哨兵 —— 求最小值初值必须"大到打不败"，
#    否则 min(0, 真实长度) 恒为 0，答案作废（求最大值则反向用 -inf）
# 2. 窗口是闭区间 [left, right]，长度 = right - left + 1（右减左要加一）
# 3. 内层必须用 while 而不是 if：删掉左端一个元素后，剩余窗口可能仍 >= target，
#    还能继续收缩 —— 这是滑动窗口两层循环的由来
# 4. 循环结束 min_len 仍是 inf ⇒ 整个数组都凑不够 target ⇒ 按题意返回 0
# 复习日期：2026-10-16

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf') #无穷大
        cur = 0

        while right < l:
            cur = cur + nums[right]
            while cur >= target:
                min_len = min(min_len , right - left + 1)
                cur = cur - nums[left]
                left = left + 1
            
            right =right + 1
        
        return min_len if min_len != float('inf') else 0

# 977. 有序数组的平方 | 数组 | 难度：简单
# 状态：✅ 暴力解独立 AC；双指针 O(n) 解法待重做（本题核心考点）
# 我的解法：原地平方 + sorted() 排序
# 时间复杂度 O(n log n)（排序主导）｜空间复杂度 O(n)（sorted 返回新数组）
#
# 【双指针思路，重做时用】
# 原数组非递减，平方后最大值必在两端之一：
#   左端是最负的数（平方可能最大），右端是最大的数（平方也最大）
# 做法：left / right 双指针对撞，比较 |nums[left]| 与 |nums[right]|，
#   大的放进结果数组末尾，对应指针向中间收 —— 从后往前填，一趟 O(n)
#
# 踩坑记录：
# 1. 没用上「原数组有序」——平方后重新 sorted，等于把题目白给的信息扔了一半
# 2. sorted() 返回新数组、不改原数组；nums.sort() 才是原地 —— 两者别混
# 3. 为什么「从后往前填」：最大值好确定（必在两端），最小值不好确定
#   （0 可能卡在中间）—— 所以填最大值容易、找最小值难，方向要选对
# 复习日期：2026-10-15

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 暴力解法
        # for i in range(0,len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # new_nums = sorted(nums)
        # return new_nums
        
        #双指针法
        #特殊情况
        if nums[0] >= 0:
            return[x ** 2 for x in nums]
        if nums[len(nums)-1] <= 0:
            return[x ** 2 for x in nums[::-1]]
        #一般情况
        i = 0
        j = len(nums) - 1
        new_nums = [0] * len(nums)
        for end_index in range(len(nums)-1,-1,-1):
            if nums[i] + nums[j] <= 0:
                new_nums[end_index] = nums[i] ** 2
                i = i + 1
            else:
                new_nums[end_index] = nums[j] ** 2
                j = j - 1
            end_index = end_index - 1
        return new_nums


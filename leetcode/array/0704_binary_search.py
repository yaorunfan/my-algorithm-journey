# 704. 二分查找 | 数组 | 难度：简单
# 思路：左闭右闭区间 [left, right]，mid 与 target 比较，每次砍掉一半
# 时间 O(log n) | 空间 O(1)
# 踩坑：`left = 0, right = ...` 逗号写法会报 can't assign to literal
#      二分必须用 // 取整，用 / 会得到小数，不能当列表下标
# 复习日期：2026-10-14

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1



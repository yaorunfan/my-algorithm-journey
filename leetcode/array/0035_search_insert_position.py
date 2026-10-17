# 35. 搜索插入位置 | 数组 | 难度：简单
# 思路：二分查找的「收敛位置」用法。循环结束时 left 就是插入位置：
#       - target 存在 → 直接 return mid
#       - target 不存在 → left 停在第一个 ≥ target 的位置
# 时间复杂度 O(log n)｜空间复杂度 O(1)
#
# 踩坑记录：
# 1. 我第一版把收尾逻辑单独拆成 while left == right，结果写成了死循环：
#    当 nums[left] == target 时没有处理，指针不动、循环条件永远成立 → TLE
# 2. 这题不需要第二个循环，标准写法就是 while left <= right + 最后 return left
# 3. 循环结束返回的是 left，不是 right，也不是 mid；left 是第一个可以放 target 的位置
# 4. 区间更新必须配套：while <= 对应 left=mid+1 / right=mid-1（左闭右闭）
# 复习日期：2026-10-18

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left  = middle + 1
            else:
                right = middle - 1
        return left
        # while left == right:
        #     if nums[left] < target:  #插在右边
        #         return  left + 1
        #     elif nums[left] > target: #插在左边
        #         if left - 1 >= 0:
        #             return left -1
        #         else:
        #             return 0
        #     else:



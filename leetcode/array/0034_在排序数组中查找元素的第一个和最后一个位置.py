# 34. 在排序数组中查找元素的第一个和最后一个位置 | 数组 | 难度：中等
# 思路：两次独立二分。找左边界时命中后继续往左压，找右边界时命中后继续往右压。
#       （不是"先找到任意一个再向两侧扩散" —— 那个做法会退化成 O(n)）
# 时间复杂度 O(log n)（两次二分各 O(log n)，常数 2 去掉）｜空间复杂度 O(1)
#
# 关键改动一句话：命中 target 时不要 return —— 记下位置，继续压缩区间。
#   findLeft ：nums[mid] == target → res = mid，然后 right = mid - 1（往左挤）
#   findRight：nums[mid] == target → res = mid，然后 left  = mid + 1（往右挤）
#   两个函数只差这一行。「找到就返回」只能得到任意一个，得靠扩散补边界，就废了。
#
# 踩坑记录：
# 1. 第一版我写的是「二分命中 + 向左右 while 扩散」，结果正确但不达标：
#    复杂度 = O(log n) + O(k)，k 是 target 出现次数；全数组都是 target 时 k = n → O(n)
#    二分省下来的时间，全赔在扩散上了。题目要求 O(log n) 就是考这一条。
# 2. 二分的区间更新必须 mid ± 1，不能写成 mid —— 否则区间不再缩小，死循环
# 3. while 用 <=（左闭右闭），对应更新 right = mid - 1 / left = mid + 1，三者要成套
# 4. mid = left + (right - left) // 2 而不是 (left + right) // 2：
#    Python 不会溢出，但 C/Java 里两数相加可能超 int 上限，面试要能说出这个理由
# 5. 找不到时 res 保持 -1，直接返回 [-1, -1]，不用单独再判
# 复习日期：2026-10-18

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #复杂度为O（logn）
        def findleft(nums,target):
            left = 0
            right =len(nums) - 1
            res = -1
            while left <= right:
                middle = left + (right - left)//2
                if nums[middle] == target:
                    res = middle
                    right = middle - 1 # 继续往左，看有没有更早的
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return res
        
        def findright(nums,target):
            left = 0
            right =len(nums) - 1
            res = -1
            while left <= right:
                middle = left + (right - left)//2
                if nums[middle] == target:
                    res = middle
                    left = middle + 1  # 继续往右，看有没有更晚的
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return res
        
        l = findleft(nums,target)
        if l == -1:
            return [-1,-1]
        return [l,findright(nums,target)]
        #复杂度为O（n）
        # def binarySearch(nums , target):
        #     left = 0
        #     right = len(nums) - 1
        #     while left <= right:
        #         middle = left + (right - left)//2
        #         if nums[middle] < target:
        #             left = middle + 1
        #         elif nums[middle] > target:
        #             right = middle - 1
        #         else:
        #             return middle
        #     return -1
        
        # index = binarySearch(nums, target)

        # if index == -1:
        #     return [-1,-1]
        # left = index
        # right = index
        # while left - 1 >= 0 and nums[left - 1] == target:
        #     left = left - 1
        # while right + 1 < len(nums) and nums[right + 1] == target:
        #     right = right + 1
        # return [left,right]
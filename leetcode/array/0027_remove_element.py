# 27. 移除元素 | 数组 | 难度：简单
# 思路：快慢双指针，慢指针指向待覆盖位置，快指针扫一遍
# 时间复杂度 O(n)｜空间复杂度 O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1
        return slow
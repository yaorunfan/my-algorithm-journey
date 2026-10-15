# 59. 螺旋矩阵 II | 数组 | 难度：中等
# 思路：模拟填数。一圈一圈往里填，每圈走「上→右→下→左」四条边，
#       统一遵守"左闭右开"，避免边界一会儿含一会儿不含。
# 时间复杂度 O(n^2)（每个格子填一次）｜空间复杂度 O(n^2)（返回矩阵本身）
#
# 关键变量：
#   startx / starty  当前这一圈的左上角起点，每走完一圈都 +1 向内收
#   offset           当前圈"右/下边界"的收缩量（等于 圈数 + 1）
#   loop = n // 2    总共要走的圈数（每圈吃掉上下左右各一层）
#   count            填数游标，从 1 一直累加到 n^2
#
# 四条边（以第 offset 圈为例，n-offset 是当前右/下边界）：
#   1) nums[startx][i]       左→右：行不变（startx），列 i 从 starty 走到 n-offset-1
#   2) nums[i][n-offset]     上→下：列不变（右边界），行 i 从 startx 走到 n-offset-1
#   3) nums[n-offset][i]     右→左：行不变（下边界），列 i 从 n-offset 回退到 starty
#   4) nums[i][starty]       下→上：列不变（starty），行 i 从 n-offset 回退到 startx
#   注意 3、4 的 range 步长是 -1（倒着走），且都是"左闭右开"，头含尾不含
#
# 中心格：n 为奇数时，走完 n//2 圈后正中间还剩一格没填，
#         填上 count（此时 count 恰好 = n^2）
#
# 踩坑记录：
# 1. range 的边界最容易错：右/下边界的"开"用 n-offset，左/上边界的"闭"用 startx/starty
# 2. 倒序 range(start, stop, -1) 是"含头不含尾"，所以 stop 写 starty/startx 才能取到
# 3. 每圈结束后 startx、starty 都要 +1，否则下一圈又从原地开始、覆盖已填的格子
# 复习日期：2026-10-17

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0] * n for _ in range (n)]
        startx = 0
        starty = 0
        loop = n//2
        mid = n//2
        count = 1
        
        for offset in range(1 , loop + 1):
            for i in range(starty , n - offset):
                nums[startx][i] = count
                count += 1
            for i in range(startx , n - offset):
                nums[i][n-offset] = count
                count += 1
            for i in range(n - offset , starty , -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset , startx , -1):
                nums[i][starty] = count
                count += 1
            
            startx += 1
            starty += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

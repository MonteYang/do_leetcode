#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.33%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    88.1K
# Total Submissions: 235.3K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        left = 1
        right = x
        while left <= right:
            # 1.如果mid的平方恰好等于x 或
            # 2.如果mid的平方小于x, 且mid+1的平方大于x,
            # 则返回mid
            mid = int((left + right)/2)
            if mid**2 == x or (mid**2 < x and (mid+1)**2 > x):
                return mid
            # 如果mid
            elif mid**2 > x:
                right = mid
            elif mid**2 < x:
                left = mid
# @lc code=end


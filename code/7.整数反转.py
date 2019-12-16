#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x):
        res = 0
        x_orig = x
        x = abs(x)
        while True:
            temp = x % 10
            x = (x - temp)/10
            res = res*10 + temp
            if x == 0:
                break

        if x_orig < 0: res = -res
        if res < -2**31 or res > 2**31-1:
            return 0
        return int(res)
            
# @lc code=end


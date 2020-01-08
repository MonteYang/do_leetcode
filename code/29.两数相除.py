#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def util(dividend, divisor):
            """ 除数倍增(×2), 获取被除数与除数间最大的2次幂倍数 """
            if dividend < divisor:
                return 0
            i = 1
            while True:
                if dividend > divisor*i*2:
                    i *= 2
                else:
                    return i
        # 获取结果的符号
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        j = 0
        while True:
            _j = util(dividend, divisor)
            j += _j
            dividend = dividend - _j*divisor
            if dividend < divisor:
                if sign*j > 2**31-1:
                    return 2**31-1
                if sign*j < -2**31:
                    return -2**31
                return sign * j
# @lc code=end

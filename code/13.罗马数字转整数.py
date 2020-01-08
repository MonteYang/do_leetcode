#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        lut = {'I': 1,
               'IV': 4,
               'V': 5,
               'IX': 9,
               'X': 10,
               'XL': 40,
               'L': 50,
               'XC': 90,
               'C': 100,
               'CD': 400,
               'D': 500,
               'CM': 900,
               'M': 1000}
        res = 0
        i = 0
        # 先判断当前输入的前两个字符是否是罗马数字,
        # if 是: 加
        # else: 将单个字符转化成数字, 加
        while i < len(s):
            if s[i:i+2] in {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}:
                res += lut[s[i:i+2]]
                i += 2
                continue
            res += lut[s[i]]
            i += 1

        return res


# @lc code=end

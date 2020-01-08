#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start


class Solution:
    def intToRoman(self, num: int) -> str:
        lut = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        res = ""
        for i in sorted(lut.keys())[::-1]:
            n, mod = divmod(num, i) 
            if n == 0:
                continue
            else:
                res += lut[i] * n
                num = mod
            if num == 0:
                break
        return res

# @lc code=end

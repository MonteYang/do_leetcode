#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (41.16%)
# Likes:    256
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 97.6K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self._dict = {}
        for i in range(10):
            self._dict.update({str(i): i})

    def multiply(self, num1: str, num2: str) -> str:
        # 使num1为长度较小的
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num2 = self.str2int(num2)
        # 将num1的每一位与num2相乘
        res = 0
        for i in range(1, len(num1)+1):
            res += self._dict[num1[-i]] * num2 * (10**(i-1))

        return str(res)

    def str2int(self, num):
        """将str类型转化为int类型"""
        ret = 0
        for i in range(1, len(num)+1):
            ret += self._dict[num[-i]] * (10**(i-1))

        return ret
# @lc code=end


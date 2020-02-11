#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (51.79%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    59.3K
# Total Submissions: 114.1K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dic = {"1": 1, "0": 0}
        i = 1
        j = 1
        res = ""
        flag = 0
        while i <= len(a) or j <= len(b):
            if i > len(a):
                tmp_a = 0
            else:
                tmp_a = dic[a[-i]]
            if j > len(b):
                tmp_b = 0
            else:
                tmp_b = dic[b[-j]]
            _sum = tmp_a + tmp_b + flag
            if _sum >= 2:
                flag = 1
                _sum %= 2
                res = str(_sum) + res
            else:
                res = str(_sum) + res
                flag = 0
            i += 1
            j += 1
        
        if flag == 1:
            res = "1" + res

        return res
# @lc code=end


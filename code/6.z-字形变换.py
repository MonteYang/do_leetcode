#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s, numRows):
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i = 0
        # 遍历字符串
        # res[0]: Z的第一行
        # res[1]: Z的第二行
        # ...
        for c in s:
            res[i] += c
            if i == 0: order_flag = True
            if i == numRows - 1: order_flag = False
            if order_flag:
                i += 1
            else:
                i -= 1
        res_str = ""
        for r in res:
            res_str += r

        return res_str
# @lc code=end

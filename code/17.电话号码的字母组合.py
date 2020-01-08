#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits):
        # digits = "324"
        if not digits:
            return []
        hashmap = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        res = [""]

        def util(res, digit):
            res_tmp = []
            # 两个for循环进行排列组合
            for s in hashmap[digit]:
                for r in res:
                    r += s
                    res_tmp.append(r)
            return res_tmp

        for i in digits:
            res = util(res, i)

        return res

# @lc code=end

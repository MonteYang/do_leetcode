#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start


class Solution:
    def isMatch(self, s, p):
        # 递归基: 都为空
        if not p:
            return not s
        # 第一个字符相互匹配
        first_match = bool(s) and p[0] in {s[0], '.'}
        # 若之后存在*  212 1*
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])

# @lc code=end

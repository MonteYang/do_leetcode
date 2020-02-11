#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (29.05%)
# Likes:    456
# Dislikes: 0
# Total Accepted:    33.5K
# Total Submissions: 115.2K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # ()()()(()()()(()))
        # 特殊情况
        if not s: return 0
        stack = []
        idxs = []
        for i in range(len(s)):
            # 如果栈为空时
            if stack == []:
                if s[i] == ')':
                    continue
                else:
                    stack.append(i)
            # 如果栈非空时
            else:
                if s[i] == ')':
                    idxs.append(i)
                    idxs.append(stack.pop())
                else:
                    stack.append(i)

        idxs.sort()

        if not idxs: return 0
        max_length = 0
        length = 1
        for j in range(0, len(idxs)-1):
            if idxs[j+1] - idxs[j] == 1:
                length += 1
            else:
                if max_length < length:
                    max_length = length
                length = 1

        return max(length, max_length)


# @lc code=end

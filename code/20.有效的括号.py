#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lut = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            # 如果输入的是左侧符号,加入栈中
            if c in lut:
                stack.append(c)
                continue
            # 如果输入的是右侧符号:
            # 如果栈中非空, 判断该符号是否与栈中最后一个符号匹配
            if stack == [] and c in lut.values():
                return False
            if len(stack) > 0 and c == lut[stack[-1]]:
                stack.pop()
            else:
                return False

        return not bool(stack)


# @lc code=end

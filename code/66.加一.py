#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (42.36%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    112.4K
# Total Submissions: 263.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        for i in range(1, len(digits)+1):
            # 最后一位加1
            if i == 1:
                digits[-i] += 1
            # 其他位加进位
            else:
                digits[-i] += flag
            # 如果当前位有进位 flag=1, 否则 flag=0
            if digits[-i] > 9:
                digits[-i] -= 10
                flag = 1
            else:
                flag = 0

        # 如果第一位仍有进位
        if flag == 1:
            digits = [1] + digits

        return digits
# @lc code=end


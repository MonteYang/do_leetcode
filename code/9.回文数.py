#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        else:
            s = str(x)
            for i in range(len(s)//2):
                if s[i] == s[-i-1]:
                    continue
                else:
                    return False 
            return True
# @lc code=end


#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
                           l0 r0
                        /          \
                       (          
                    l1 r0           
                    /   \        
                  ((     ()         
                l2 r0   l1 r1
                ...
        """
        res = []

        def util(cur_str, n_lb, n_rb):
            if n_lb > n or n_rb > n:
                return
            if n_lb == n_rb == n:
                res.append(cur_str)
            if n_lb == n_rb:
                util(cur_str+'(', n_lb+1, n_rb)
            if n_lb > n_rb:
                util(cur_str+'(', n_lb+1, n_rb)
                util(cur_str+')', n_lb, n_rb+1)
            if n_lb < n_rb:
                return

        util('', 0, 0)
        return res

# @lc code=end

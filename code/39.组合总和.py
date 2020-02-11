#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (67.80%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 85.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：


# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 


# 示例 1:

# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]


# 示例 2:

# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]

#
from typing import List
import copy
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def util(candidates, cur_sum, tmp_list):
            if candidates == []: return

            # 如果当前列表之和等于 target, 加入res
            if cur_sum == target:
                res.append(tmp_list)

            # 如果当前列表元素之和大于 target，直接返回（剪枝）
            elif cur_sum > target:
                return
            
            # 如果当前列表元素之和小于 target，继续添加元素
            else:
                for i, c in enumerate(candidates):
                    _tmp_list = copy.deepcopy(tmp_list)
                    _tmp_list.append(c)
                    util(candidates[i:], cur_sum+c, _tmp_list)
        
        util(candidates, 0, [])
        return res
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print("res", s.combinationSum([2,3,6,7], 7))

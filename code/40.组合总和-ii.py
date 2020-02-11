#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (59.21%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    36.2K
# Total Submissions: 60.9K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # [1,1,2,5,6,]
        
        def back_track(cur_sum, cur_list, candidates):
            # 如果当前总和等于target, 则将当前list添加至res中
            if cur_sum == target:
                res.append(cur_list)
            # 如果当前总和大于target, 则减枝
            elif cur_sum > target:
                return
            # 如果当前总和小于target, 继续在list中添加元素
            else:
                for i, c in enumerate(candidates):
                    if i > 0 and c == candidates[i-1]: continue
                    _cur_list = cur_list[:]
                    _cur_list.append(c)
                    back_track(cur_sum+c, _cur_list, candidates[i+1:])
        
        back_track(0, [], candidates)

        return res
# @lc code=end


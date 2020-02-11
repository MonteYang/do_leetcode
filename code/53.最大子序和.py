#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.59%)
# Likes:    1547
# Dislikes: 0
# Total Accepted:    149.7K
# Total Submissions: 306.6K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 特殊情况: nums为空
        if not nums:
            return []
        # res = []
        # res_tmp = []
        ans_sum = 0
        max_sum = float('-inf')
        for n in nums:
            # 如果当前之和大于0
            if ans_sum >= 0:
                # 先添加至 res_tmp 中
                # res_tmp.append(n)
                ans_sum += n
            # 如果当前之和小于0
            else:
                # res_tmp = [n]
                ans_sum = n
            # 如果当前之和大于保存的最大和, 则将最大和替换, res也同时替换
            if ans_sum > max_sum:
                max_sum = ans_sum
                # res = res_tmp[:]  # 此处不能直接赋值, 需复制list内容/deepcopy
        return max_sum
# @lc code=end


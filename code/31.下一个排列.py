#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
"""
字典序算法:
1. 从右往左, 找出第一个小于右邻的数 list[x];
2. 从右往左, 找出第一个比 list[x] 大的数 list[y];
3. 交换 list[x] 和 list[y];
4. 将 list[x] 后面的序列从小到大排序. 
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return 
        # 1
        x = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                x = i
                break
        # 如果不存在下一个更大的字典序(即当前序列为最大的字典序), 则将序列转为最小字典序
        if x == -1:
            nums.sort()
            return 
        # 2
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[x]:
                y = i
                break
        # 3, 4
        nums[x], nums[y] = nums[y], nums[x]
        nums[x+1:] = sorted(nums[x+1:])


# @lc code=end


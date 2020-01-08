#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = - float("inf")
        i = 0
        while True:
            try:
                # 如果第i个数和判断相等, 删除第i个数
                if nums[i] == p:
                    del nums[i]
                # 如果不等, 保留
                else:
                    p = nums[i]
                    i += 1
            except Exception:
                break
        length = len(nums)
        return length
# @lc code=end

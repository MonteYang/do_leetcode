#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            # 如果第i个元素等于目标值val, 跳过
            if nums[i] == val:
                continue
            # 如果第i个元素不等于目标值val, 从头依次添加到原list中
            else:
                nums[j] = nums[i]
                j += 1

        return j

        
# @lc code=end


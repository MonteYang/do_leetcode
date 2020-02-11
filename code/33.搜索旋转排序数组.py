#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.22%)
# Likes:    460
# Dislikes: 0
# Total Accepted:    64.7K
# Total Submissions: 178.6K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [4,5,6,7,0,1,2]
        if not nums: return -1
        # 找出最小值的索引
        min_idx = self.search_min_idx(nums)
        if min_idx != 0:
            nums = nums[min_idx:] + nums[:min_idx]
        # 二分查找
        tmp_idx = self.bin_search(nums, target)
        if tmp_idx == -1: return -1
        return (tmp_idx + min_idx) % len(nums)

    def search_min_idx(self, nums):
        # TODO: 
        return nums.index(min(nums))

    def bin_search(self, nums, target):
        """
        二分查找法:
            - 如果nums中存在目标值, 则返回该值的index;
            - 如果nums中不存在目标值, 则返回 -1.
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return -1


# @lc code=end

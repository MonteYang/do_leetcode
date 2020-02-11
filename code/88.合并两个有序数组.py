#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (46.09%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    102.9K
# Total Submissions: 221.9K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 指针 i 遍历 nums1, 指针 j 遍历 nums2
        i, j = 0, 0
        nums_tmp = []
        while i < m and j < n:
            # 如果nums2中当前元素 < nums1中当前元素, 交换这两个数, i向后移动一个单位
            if nums1[i] <= nums2[j]:
                nums_tmp.append(nums1[i])
                i += 1
            else:
                nums_tmp.append(nums2[j])
                j += 1
        # 如果i或j遍历结束,还有剩余
        if i == m: nums_tmp += nums2[j:n]
        if j == n: nums_tmp += nums1[i:m]

        nums1[:] = nums_tmp

# @lc code=end


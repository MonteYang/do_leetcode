#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums):
        """ 返回一组数中之和为0的三个数(list of lists).
        解法: 排序 + 使用双指针

        Args:
            nums (list): a list of nums

        Returns:
            list: 每个元素都是3个数且3个数之和为0
        """
        # 如果不够3个元素, 则返回空
        res = []
        if len(nums) < 3:
            return res
        nums = sorted(nums)  # [-4, -1, -1, 0, 1, 2, ]
        # 确定第一个元素, 第一层遍历
        for i in range(len(nums)):
            # 如果所有元素都大于等于0, 则返回
            if nums[i] > 0:
                return res
            # !!! 去重方法: 排好序后,相等则跳过...
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 确定双指针, 一个最左(i+1), 一个最右[-1]
            pt_left = i + 1
            pt_right = len(nums) - 1

            # 如果 三数之和等于0, 添加至res列表, 左右指针都到下一个位置
            # 如果 三数之和大于0, 右指针往左一个单位, 整体变小
            # 如果 三数之和小于0, 左指针往右一个单位, 整体变大
            while pt_left < pt_right:
                if nums[i] + nums[pt_left] + nums[pt_right] == 0:
                    res.append([nums[i], nums[pt_left], nums[pt_right]])
                    while nums[pt_left] == nums[pt_left+1] and pt_left < pt_right-1:
                        pt_left += 1
                    while nums[pt_right] == nums[pt_right-1] and pt_left < pt_right-1:
                        pt_right -= 1
                    pt_left += 1
                    pt_right -= 1

                elif nums[i] + nums[pt_left] + nums[pt_right] > 0:
                    while nums[pt_right] == nums[pt_right-1] and pt_left < pt_right-1:
                        pt_right -= 1
                    pt_right -= 1
                else:
                    while nums[pt_left] == nums[pt_left+1] and pt_left < pt_right-1:
                        pt_left += 1
                    pt_left += 1

        return res


# @lc code=end

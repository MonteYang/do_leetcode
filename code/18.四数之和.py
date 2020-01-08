#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start


class Solution:
    def fourSum(self, nums, target):
        """ 在list of nums中,获取能够使得和为target的四元组.

        Args:
            nums (List[int]): 一组数.
            target (int): list of lists, int.

        Returns:
            List[List[int]]: 所有和为target的四元组.
        """
        res = []
        # 特殊情况, nums中少于4个数
        if len(nums) < 4:
            return res
        # 1. 排序
        nums = sorted(nums)
        for i in range(len(nums)-3):
            # 避免重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # 避免重复
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # 双指针: L-左指针, R-右指针
                L = j + 1
                R = len(nums) - 1
                # (左指针向右移,右指针向左移)当左指针超过右指针时,break.
                while L < R:
                    # 如果四数之和等于target,则添加
                    if nums[i] + nums[j] + nums[L] + nums[R] == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        # 避免重复
                        while nums[L] == nums[L+1] and L < R-1:
                            L += 1
                        L += 1
                        while nums[R] == nums[R-1] and L < R-1:
                            R -= 1
                        R -= 1
                    # 如果四数之和小于target,则左指针向右移动
                    elif nums[i] + nums[j] + nums[L] + nums[R] < target:
                        # 避免重复
                        while nums[L] == nums[L+1] and L < R-1:
                            L += 1
                        L += 1
                    # 如果四数之和大于target,则右指针向左移动
                    else:
                        # 避免重复
                        while nums[R] == nums[R-1] and L < R-1:
                            R -= 1
                        R -= 1
        return res


# @lc code=end

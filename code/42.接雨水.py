#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.85%)
# Likes:    810
# Dislikes: 0
# Total Accepted:    48.8K
# Total Submissions: 101.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        water_sum = 0
        left_max_height = 0
        # 遍历从 idx=1 到 idx=leng(height)-2
        for i in range(1, len(height) - 1):
            # 求左边最高的墙高
            left_max_height = height[i - 1] \
                 if height[i - 1] > left_max_height else left_max_height
            # 求右边最高的墙高
            right_max_height = 0
            right_max_height = max(height[i+1:])
            # 当前列可容纳的水量
            water = max(min(left_max_height, right_max_height) - height[i], 0)
            water_sum += water

        return water_sum


# @lc code=end

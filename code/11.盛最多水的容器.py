#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    # 暴力法
    '''
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(min(height[i], height[j]) * (j - i), max_area)

        return max_area
    '''
    # 双指针法
    # - 一般来说,距离最远的围成较大面积的可能性较大
    # - 两头各放一个指针
    # - 较短一侧的指针往里移动, 才可能使面积变大(虽然两指针距离变短,但是较短一侧的高度可能变大)

    def maxArea(self, height):
        pt_left = 0
        pt_right = len(height) - 1
        max_area = 0
        while True:
            # 新算的面积 = min(height[pt_left], height[pt_right])*(pt_right - pt_left)
            # 最大面积 = max(新算的面积, 原来的最大面积)
            max_area = max(min(height[pt_left], height[pt_right])*(pt_right - pt_left), max_area)

            # 选取较小一侧的指针,往内移动一个单位
            if height[pt_left] < height[pt_right]:
                pt_left += 1
            else:
                pt_right -= 1

            # 指针汇合时, 循环结束
            if pt_left == pt_right:
                break
        return max_area


# @lc code=end

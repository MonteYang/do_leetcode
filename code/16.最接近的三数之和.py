#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return False
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)

        min_dist = float('inf')
        for i in range(len(nums)):
            # 重复的则跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            # 双指针
            while L < R:
                _sum = nums[i] + nums[L] + nums[R]
                delta = _sum - target
                # 如果两数之差小于最小值,保存该sum为res
                if abs(delta) < min_dist:
                    res = _sum
                    min_dist = abs(delta)
                # 三数之和大于target,
                if delta > 0:
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    R -= 1
                # 三数之和小于target
                elif delta < 0:
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    L += 1
                else:
                    return _sum
        return res

if __name__ == "__main__":
    s = Solution()
    nums =[6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]


    print(s.threeSumClosest(nums, -52))

# @lc code=end


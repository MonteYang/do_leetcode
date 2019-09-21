# coding: utf-8
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
'''


class Solution:
    def twoSum(self, nums, target):
        # 哈希表,反过来存 num -> idx, 有可能同一num对应多个idx, 所以 {12: [idx1, idx2, ...]}
        hashmap = {}
        for i, n in enumerate(nums):
            if n not in hashmap:
                hashmap[n] = [i]
            else:
                hashmap[n].append(i)

        for num_1, idx_1 in hashmap.items():
            # num_2 = target - num_1 , 在hashmap中
            if target - num_1 in hashmap:
                # num_1 与 num_2 数值相等时
                if (target - num_1 == num_1):
                    # [注意] 如果找到的 num_2 其实是 num_1 自己, 跳过...
                    if (len(hashmap[num_1]) == 1):
                        continue
                    # num_2 与 num_1 不同
                    if len(hashmap[target-num_1]) >= 2:
                        return hashmap[target-num_1][0], hashmap[target-num_1][1]
                # num_2 与 num_1 不同
                else:
                    return idx_1[0], hashmap[target-num_1][0]
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))

# coding: utf-8
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        length = len(nums1) + len(nums2)
        p1, p2 = 0, 0
        for _ in range(int(length/2)+1):
            if nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        if length % 2 == 0:
            median = (nums[-1] + nums[-2])/2
        else:
            median = nums[-1]

        return median


if __name__ == "__main__":
    nums1 = [1, 3, 5]
    nums2 = [2, 3, 6]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))

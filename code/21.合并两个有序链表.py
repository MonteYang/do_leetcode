#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        p1 = l1
        p2 = l2
        head = ListNode("#")
        cur = head

        while p1 or p2:
            if (p2 is None and p1) or (p1 and (p1.val <= p2.val)):
                cur.next = ListNode(p1.val)
                cur = cur.next
                p1 = p1.next
            if (p1 is None and p2) or (p2 and (p2.val < p1.val)):
                cur.next = ListNode(p2.val)
                cur = cur.next
                p2 = p2.next
            
        return head.next
# @lc code=end

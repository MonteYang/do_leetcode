#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd(self, head, n):
        # 链表长度
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next
        # 特殊情况
        if n == len(arr) == 1:
            return None
        if n == len(arr):
            head = arr[1]
            return head
        node_to_del = arr[-n]
        arr[-n-1].next = node_to_del.next

        return head

# @lc code=end

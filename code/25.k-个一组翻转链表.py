#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        TH = ListNode('#')
        TH.next = head
        p = TH
        while True:
            # 判断从节点开始到最后一个小于k,
            if self.less_than_k(p, k):
                break
            # 翻转具有k个结点的链表
            i = 0
            while i <= k:

    def less_than_k(self, p, k):
        cnt = 0
        while p.next:
            p = p.next
            cnt += 1
            if cnt >= k:
                return True

        return False


# @lc code=end

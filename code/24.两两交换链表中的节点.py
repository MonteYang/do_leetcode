#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        p_head  ->   1    ->     2    ->    3   ->  4
        (p)     ->   q    ->     r    ->    s 
                          ->    (p)   ->    q   ->  r 
        """
        # 设置头结点,方便后续处理
        p_head = ListNode('#')
        p_head.next = head

        # 如图设置p,q,r,s的指向
        p = p_head
        q = p.next
        while q:
            r = q.next
            if not r:  # 奇数个结点则跳出
                break
            # 交换
            s = r.next
            r.next = q
            q.next = s
            p.next = r
            # 移动指针p的指向
            p = p.next.next
            q = p.next
        # 必须返回p_head.next, 不能返回head, 因为head已经在链表中被交换.
        return p_head.next


# @lc code=end

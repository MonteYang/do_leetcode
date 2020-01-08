#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
class Solution:
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_p = []
        for p in lists:
            if p:
                list_p.append(p)
            else:
                continue

        if not list_p: return None

        res_head = ListNode("#")
        node = res_head

        while True:
            # 找出最小元素的索引
            list_p_val = [p.val for p in list_p]
            if not list_p_val:
                break
            min_idx = list_p_val.index(min(list_p_val))

            # 添加到新建链表尾部
            node.next = ListNode(list_p[min_idx].val)
            node = node.next

            if not list_p[min_idx].next:
                del list_p[min_idx]
            else:
                list_p[min_idx] = list_p[min_idx].next

        return res_head.next
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 特殊情况: lists为空
        if not lists: return None
        # 对所有val进行排序
        val_all = []
        for node in lists:
            while True:
                if node:
                    val_all.append(node.val)
                    node = node.next
                else:
                    break
        val_all = sorted(val_all)
        # 生成整个链表
        head = ListNode('#')
        node = head
        for v in val_all:
            node.next = ListNode(v)
            node = node.next

        return head.next
# @lc code=end


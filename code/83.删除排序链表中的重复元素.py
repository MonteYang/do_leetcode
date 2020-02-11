#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (48.64%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    68.7K
# Total Submissions: 140.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # _head = ListNode("*")
        # _head.next = head
        node = head
        while node and node.next:
            # 如果当前值等于下一个结点的值,将下一个结点删除
            if node.val == node.next.val:
                # 删除下一个结点
                if not node.next.next:
                    node.next = None
                else:
                    node.next = node.next.next
            # 如果当前结点不等于下一结点,迭代下一个结点
            else:
                node = node.next

        return head
        
# @lc code=end


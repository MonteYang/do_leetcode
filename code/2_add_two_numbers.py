# coding: utf-8
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1, num2 = '', ''
        while l1:
            num1 = num1 + str(l1.val)
            l1 = l1.next

        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next

        num1 = int(str(num1)[::-1])
        num2 = int(str(num2)[::-1])

        string = str(num1 + num2)[::-1]
        node_list = [ListNode(int(s)) for s in string]

        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]

        return node_list[0]
'''


class Solution:
    def addTwoNumbers(self, l1, l2):
        HeadNode = ListNode(0)
        cur = HeadNode
        carry = 0
        # 技巧: 迭代2个链表的同时进行计算,存入result链表,使算法复杂度降低.
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_cur = x + y + carry
            carry = 0
            if sum_cur >= 10:
                carry = 1
                sum_cur %= 10
            cur.next = ListNode(sum_cur)
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
            cur = cur.next
        # l1,l2都迭代完, 但是最后有进位时
        if carry:
            cur.next = ListNode(carry)

        return HeadNode.next

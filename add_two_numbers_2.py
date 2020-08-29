"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Runtime: 84ms (53.4%)
# Memory Distribution: 13.9 MB (43.85%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sl1 = []
        sl2 = []
        carry = 0
        l3 = ListNode(-1)
        while l1:
            sl1 += [l1.val]
            l1 = l1.next
        while l2:
            sl2 += [l2.val]
            l2 = l2.next
        print(sl1)
        print(sl2)
        while sl1 or sl2:
            if not sl2:
                val = sl1.pop()
            elif not sl1:
                val = sl2.pop()
            else:
                val = sl1.pop() + sl2.pop()
            val += carry
            if val > 9:
                val -= 10
                carry = 1
            else:
                carry = 0
            l3.val = val
            temp = l3
            l3 = ListNode(-1)
            l3.next = temp
            if carry:
                l3.val = carry
        if l3.val == -1:
            return l3.next
        return l3
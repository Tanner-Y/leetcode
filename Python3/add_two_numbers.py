# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodes = []
        cl1 = l1
        cl2 = l2
        carry = []
        val = 0
        while cl1 or cl2:
            v1, v2 = 0, 0
            val = 0
            try:
                v1 = cl1.val
            except AttributeError:
                pass
            try:
                v2 = cl2.val
            except AttributeError:
                pass
            val = v1 + v2
            if val >= 10:
                val -= 10
                carry.append(1)
            else:
                carry.append(0)
            try:
                val += carry[-2]
                if val >= 10:
                    val -= 10
                    carry.append(1)
            except:
                pass
            nodes.append(ListNode(val))
            try:
                cl1 = cl1.next
            except AttributeError:
                pass
            try:
                cl2 = cl2.next
            except AttributeError:
                pass
        if carry[-1] == 1:
            nodes.append(ListNode(1))
        for n in range(len(nodes)-1):
            nodes[n].next = nodes[n+1]
        return nodes[0]

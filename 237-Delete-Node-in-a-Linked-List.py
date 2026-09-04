# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # time: O(n)
        # space: O(1)

        current = node

        while current.next:
            current.val = current.next.val
            if current.next.next is None:
                current.next = None
            else:
                current = current.next   

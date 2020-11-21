# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        lenNode = head
        while lenNode != None:
            length += 1
            lenNode = lenNode.next

        result = 0
        degree = 2 ** (length - 1)
        node = head
        while node != None:
            result += node.val * degree
            degree = degree // 2
            node = node.next

        return result

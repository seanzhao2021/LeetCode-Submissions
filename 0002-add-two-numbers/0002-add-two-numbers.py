# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tempHead = ListNode(0)
        curr = tempHead
        carry = 0
        while l1 != None or l2 != None or carry!= 0:
            Val1 = l1.val if l1 != None else 0
            Val2 = l2.val if l2 != None else 0
            colSum = Val1 + Val2 + carry
            carry = colSum / 10
            newNode = ListNode(colSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return tempHead.next



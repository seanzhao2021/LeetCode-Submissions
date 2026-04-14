# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        #two pointers, fast and slow
        fast = head
        fastIdx = 0
        slow = head
        #fast needs to be n nodes ahead of slow
        #once fast reaches the end, we know that slow is ON the node to remove
        
        prev = None
        while fast:
            if fastIdx >= n:
                #update both
                fast = fast.next
                #update slow with a prev pointer
                temp = slow.next
                prev = slow
                slow = temp
            else:
                #only update fast for now
                fastIdx += 1
                fast = fast.next

        #if prev is None, slow has not moved, need to delete head
        #return head.next
        if not prev:
            return head.next

        #prev.next = slow.next
        #slow.next = None
        prev.next = slow.next
        slow.next = None

        return head
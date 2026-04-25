# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        #function to merge two lists
        def merge(head1, head2):
            prev = ListNode()
            head = prev
            
            while(head1 and head2):

                if head2.val > head1.val:
                    temp = head1.next
                    prev.next = head1
                    prev = prev.next
                    head1 = temp
                else:
                    temp = head2.next
                    prev.next = head2
                    prev = prev.next
                    head2 = temp

            #if head1 is None connect the rest to head2
            #if head2 is None connect the rest to head1
            if head1:
                prev.next = head1
            else:
                prev.next = head2
            
            return head.next



        #for i in range len(list) - 1 (3 lists means we run twice)
        for i in range(len(lists) - 1):
            #merge(i, i + 1)
            temp = merge(lists[i], lists[i + 1])
            #make i + 1 point to new merged list node
            lists[i + 1] = temp

        
        if not lists:
            return None
        else:
            return lists[-1]
        
        
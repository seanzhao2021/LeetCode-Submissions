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

        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                print(i)
                print(i + 1)
                if i + 1 >= len(lists):
                    merged.append(lists[i])
                else:
                    merged.append(merge(lists[i], lists[i + 1]))
            lists = merged



        
        if not lists:
            return None
        else:
            return lists[-1]
        
        
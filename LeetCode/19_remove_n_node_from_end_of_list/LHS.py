# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ## len == 1 case
        if head.next == None:
            return None
        
        ## return the length of the linked-list
        def len_of_list(head):
            cnt = 1
            point = head
            while(point.next != None):
                point = point.next
                cnt += 1
            return cnt    
        cnt = len_of_list(head)
        
        ## when the top is out
        if cnt == n:
            return head.next

        ## iterate whole list and pass n-th from end
        point = head
        for i in range(cnt-1):
            if i == cnt-n-1:
                point.next = point.next.next
            point = point.next

        return head

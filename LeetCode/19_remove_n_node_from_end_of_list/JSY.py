# Retrospect
# 1. removeNthFromEnd 안에 self 들어감. => 당연히 instantiate 해서 써야 함
# 2. python object 의 attribute 보는 방법: dir(object)
# 3. node 순회할 때, 다음 노드로 가는 로직 꼭 넣어야 함! 
# 4. edge case


import typing
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # From head, should call 'next' (sz - n) times
        # at (sz-n-1) time's call, should save the prev node
        
        if head.next is None: # 1-element list
            return None
        
        # First, should figure out the length of this list
        curr = head
        sz = 1
        
        while curr.next != None:
            sz += 1
            curr = curr.next #NOTE: 여기가 실수

        if sz == n: # should remove the first element
            temp = head
            head = temp.next
            temp.next = None
            del temp

            return head
            
        else: 
            # Remove the Nth node 
            curr = head
            for _ in range(sz - n - 1):
                curr = curr.next
            
            # Now at prev node
            prev = curr

            # Hop to the target node
            target = curr.next
            
            # Connect the prev and targets' next node
            prev.next = target.next

            # delete the target object
            target.next = None
            del target

            return head

    def printAllNodes(self, head) -> None:
        print(type(head))
        curr = head
        while curr.next != None:
            # print(curr.val)
            curr = curr.next
        # print(curr.val)



if __name__ == "__main__":
    solution = Solution()

    # Testset 1
    # N = 2
    # n5 = ListNode(5)
    # n4 = ListNode(4, n5)
    # n3 = ListNode(3, n4)
    # n2 = ListNode(2, n3)
    # n1 = ListNode(1, n2)

    # Testset 2
    # N = 1
    # n1 = ListNode(1)

    # Testset 3
    N = 1
    n2 = ListNode(2)
    n1 = ListNode(1, n2)


    head = solution.removeNthFromEnd(n1, N)
    solution.printAllNodes(head)
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. store all nodes in 'nodes' list
        nodes = []
        nodes.append(head)
        curr_node = head
        while (curr_node.next != None):
            nodes.append(curr_node.next)
            curr_node = curr_node.next
        
        # 2. change pointers (handle edge cases!)
        target_idx = len(nodes) - n 
        if target_idx == 0:
            return head.next
        elif target_idx == len(nodes)-1:
            nodes[target_idx-1].next = None
        else:
            nodes[target_idx-1].next = nodes[target_idx+1]
        return head


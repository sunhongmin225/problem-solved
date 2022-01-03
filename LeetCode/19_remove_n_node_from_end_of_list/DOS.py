from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val}, {self.next})"


class Solution:
    def get_length(self, head):
        length = 0
        current_node = head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def get_linked_list_head(self, seqeunce: deque):
        result = None
        if not seqeunce:
            return result
        element = seqeunce.popleft()
        result = ListNode(element, self.get_linked_list_head(seqeunce))
        return result

    def removeNthFromEnd(self, head, n: int):
        length = self.get_length(head)
        if n == length == 1:
            return None
        current = head
        result = deque()
        target_idx = length - n

        i = 0
        while current is not None:
            if current is not None and i != target_idx:
                result.append(current.val)
            current = current.next
            i += 1
        return self.get_linked_list_head(result)


if __name__=="__main__":

    e = ListNode(5)
    d = ListNode(4,e)
    c = ListNode(3,d)
    b = ListNode(2,c)
    a = ListNode(1,b) # head
    res = Solution().removeNthFromEnd(a, 2)
    print(f"{res=}") # [1,2,3,5]

    e = ListNode(5)
    d = ListNode(4,e)
    c = ListNode(3,d)
    b = ListNode(2,c)
    a = ListNode(1,b) # head
    res = Solution().removeNthFromEnd(a, 5)
    print(f"{res=}") # [2,3,4,5]

    e = ListNode(5)
    d = ListNode(4,e)
    c = ListNode(3,d)
    b = ListNode(2,c)
    a = ListNode(1,b) # head
    res = Solution().removeNthFromEnd(a, 4)
    print(f"{res=}") # [1,3,4,5]

    a = ListNode(1) # head
    res = Solution().removeNthFromEnd(a, 1)
    print(f"{res=}") # []

    b = ListNode(2) # head
    a = ListNode(1, b) 
    res = Solution().removeNthFromEnd(a, 1)
    print(f"{res=}") # [1]

    b = ListNode(2) # head
    a = ListNode(1, b) 
    res = Solution().removeNthFromEnd(a, 2)
    print(f"{res=}") # [2]
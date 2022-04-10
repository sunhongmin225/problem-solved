from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dq = deque(nums)
        k = k % len(nums)
        for _ in range(k):
            dq.appendleft(dq.pop())
        nums[:] = list(dq)


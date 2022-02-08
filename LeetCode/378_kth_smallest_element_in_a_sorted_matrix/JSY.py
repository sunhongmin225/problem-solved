from queue import PriorityQueue
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        que = PriorityQueue()

        ROWS, COLS = len(matrix), len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                que.put(matrix[i][j])
        
        ans = 0
        for i in range(k):
            que.get()
            if i == k - 1:
                ans = que.get()

        return ans

if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8

    print(Solution().kthSmallest(matrix, k))

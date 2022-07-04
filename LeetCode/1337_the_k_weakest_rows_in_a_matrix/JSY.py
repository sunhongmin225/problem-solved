from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ROW, COL = len(mat), len(mat[0])
        lst = []

        for i in range(ROW):
            lst.append((i, sum(mat[i]))) # (row_index, num_soldiers)
        
        # sort with repect to the second element (num_soldiers)
        lst.sort(key=lambda x:x[1])
        
        top_k_rows = [row_index for row_index, _ in lst[:k]]
        return top_k_rows


if __name__ == "__main__":
    mat = [[1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]]
    k = 3
    print(Solution().kWeakestRows(mat, k))

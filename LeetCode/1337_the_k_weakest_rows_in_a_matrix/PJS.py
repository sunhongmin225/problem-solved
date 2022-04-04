class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_soldiers = []
        for i, row in enumerate(mat):
            num_soldiers.append((i, row.count(1)))
        
        weakest_soldiers = []
        while(len(weakest_soldiers) < k):
            least_num = 101
            least_idx = 0
            
            min_idx = 0
            for i, item in enumerate(num_soldiers):
                if item[1] < least_num:
                    least_num = item[1]
                    least_idx = item[0]
                    min_idx = i
                elif item[1] == least_num and item[0] < least_idx:
                    least_idx = item[0]
                    min_idx = i
            weakest_soldiers.append(least_idx)
            num_soldiers.pop(min_idx)
            
        return weakest_soldiers

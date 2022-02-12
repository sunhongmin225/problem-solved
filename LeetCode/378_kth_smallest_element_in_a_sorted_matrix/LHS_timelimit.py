class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
       
        # binary search
        def find_index(ans, val, low, high):
            if val >= ans[high]:
                return high+1
            
            while low < high:
                mid = int((low + high)/2)
                if val < ans[mid]:
                    high = mid
                else:
                    low = mid + 1
            return low
        
        ans = [0 for i in range(n**2)]
        for i in range(n):
            for j in range(n):
                # the first row can be added directly
                if i == 0:
                    ans[n*i+j] = matrix[i][j]
                else:
                    # when j is 0 (first column), start searching from index 1 to right before
                    if j == 0:
                        idx = find_index(ans, matrix[i][j], 1, i*n-1)
                    else:
                    # else case: save previous index and use it as start index
                        prev_idx = idx
                        idx = find_index(ans, matrix[i][j], prev_idx, i*n-1+j)
                 
                    ans[idx+1:-1] = ans[idx:-2]
                    ans[idx] = matrix[i][j]
        return(ans[k-1])

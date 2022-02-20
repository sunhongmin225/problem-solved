# memory complexity < O(n^2) --> cannot store indices or tuples to keep track
# binary search..?

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # instead of keeping an index as a midpoint, keep the actual value
        min_value = matrix[0][0]
        max_value = matrix[-1][-1]
        
        while(min_value <= max_value):
            # find the average of the min and max values
            mid_value = (min_value + max_value) // 2
            cnt = 0
            
            # counts the number of elements in the matrix that are smaller (or equal to) the mid_value
            for row in matrix:
                for value in row:
                    if value > mid_value:
                        break
                    else:
                        cnt += 1
            
            # if the count is smaller than k, it means we need to search the part larger than mid_value
            # else, we need to search the part smaller than mid_value
            if cnt < k:
                min_value = mid_value + 1
            else:
                # if cnt == k (when min_value == kth smallest), 
                # max_value will be finally deducted by 1, and the while loop will break
                max_value = mid_value - 1
            
        return min_value

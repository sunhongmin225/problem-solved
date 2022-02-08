from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        if N == 1: return matrix[0][0]
        elif k == 1: return matrix[0][0]
        else:
            nx = [0, 1]
            ny = [1, 0]

            candidates = []
            x, y, smallest = 0, 0, 0

            while (k > 1):
                for i in range(2):
                    r = x + nx[i]
                    c = y + ny[i]
                
                    if r < N and c < N and (r, c) not in candidates:
                        candidates.append((r, c))

                # Find the smallest element among candidates
                random_item = candidates[0]
                smallest = matrix[random_item[0]][random_item[1]]
                x = random_item[0]
                y = random_item[1]

                for candidate in candidates:
                    x_ = candidate[0]
                    y_ = candidate[1]
                    if matrix[x_][y_] < smallest:
                        smallest = matrix[x_][y_]
                        x = x_
                        y = y_

                candidates.remove((x, y))
                k -= 1
            
            return smallest

if __name__ == "__main__":
    # matrix = [[-5]]
    # k = 1

    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8

    print(Solution().kthSmallest(matrix, k))

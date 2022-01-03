class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result = []
        rotated_tuple = list(zip(*matrix[::-1]))
        for t in rotated_tuple:
            result.append(list(t))

        return result



if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    [[7,4,1],[8,5,2],[9,6,3]]
    print(Solution().rotate(matrix))

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(matrix)
    [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(Solution().rotate(matrix))

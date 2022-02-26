class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first_letter_location = []
        m = len(board)
        n = len(board[0])
        
        # first, get the positions of the first letter
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    first_letter_location.append((i, j))
        
        for loc in first_letter_location:
            # visited tags 1 for those locations on the board that are visited
            visited = [[0]*n for _ in range(m)]
            
            def exist_next_letter(i, j, idx):
                # i, j is the current location, and idx is the index of character within 'word' 
                # that is to be checked next.

                if idx == len(word):
                    # reaching here means we've succeeded in finding the whole word on the board
                    return True
                
                if i-1 >= 0 and visited[i-1][j] != 1 and board[i-1][j] == word[idx]:
                    visited[i-1][j] = 1
                    if exist_next_letter(i-1, j, idx+1):
                        return True
                    visited[i-1][j] = 0
                    
                if i+1 < m and visited[i+1][j] != 1 and board[i+1][j] == word[idx]:
                    visited[i+1][j] = 1
                    if exist_next_letter(i+1, j, idx+1):
                        return True
                    visited[i+1][j] = 0
                    
                if j-1 >= 0 and visited[i][j-1] != 1 and board[i][j-1] == word[idx]:
                    visited[i][j-1] = 1
                    if exist_next_letter(i, j-1, idx+1):
                        return True
                    visited[i][j-1] = 0
                    
                if j+1 < n and visited[i][j+1] != 1 and board[i][j+1] == word[idx]:
                    visited[i][j+1] = 1
                    if exist_next_letter(i, j+1, idx+1):
                        return True
                    visited[i][j+1] = 0
                    
                return False
            
            visited[loc[0]][loc[1]] = 1
            # recursively check for next letters
            result = exist_next_letter(loc[0], loc[1], 1)
            if result is True:
                return True
            
        return False

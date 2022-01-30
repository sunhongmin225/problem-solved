# 79. Word Search

## Link
https://leetcode.com/problems/word-search/

## Problem
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example 1
![image](https://user-images.githubusercontent.com/44546247/151698971-ea17652a-5230-4e52-9f8d-4dcdaa01adcd.png)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```


### Example 2
![image](https://user-images.githubusercontent.com/44546247/151698997-494dfc24-5b12-4dee-a964-584697b63c3f.png)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```


### Example 3
![image](https://user-images.githubusercontent.com/44546247/151699038-c9319b64-5c88-4ffa-a862-dd933a81f100.png)
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```


## Constraints
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.
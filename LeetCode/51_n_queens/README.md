# 51. N-Queens

## Link
https://leetcode.com/problems/n-queens/


## Problem
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

### Example 1
![Screen Shot 2022-01-23 at 3 43 54 PM](https://user-images.githubusercontent.com/54504359/150667772-0c2fa83a-a831-44a9-ad6e-da9782bec2d0.png)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```


### Example 2
```
Input: n = 1
Output: [["Q"]]
```

## Constraints
- `1 <= n <= 9`


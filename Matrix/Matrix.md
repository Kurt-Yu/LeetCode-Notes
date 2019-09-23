# Matrix

## Traversal

### [Leetcode 62. Unique Paths](https://leetcode.com/problems/unique-paths/)
> A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

> The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

> How many possible unique paths are there?

```python
def uniquePaths(self, m, n):
    matrix = [[1] * m for _ in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0: matrix[i][j] = matrix[i - 1][j] if i > 0 else 1
            elif j == 0: matrix[i][j] = matrix[i][j - 1] if j > 0 else 1
            else: matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    return matrix[-1][-1]
```


## Search

### [Leetcode 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
> Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
```
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
```
**Solution:** This is essentially a binary search problem. Treat the matrix as a flattened array, the lower bound is `0`, upper bound is `row * col - 1`. The rest is just like doing a normal binary search on an array.

```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]: return False
    
    row, col = len(matrix), len(matrix[0])
    i, j = 0, row * col - 1
    
    while i <= j:
        mid = (i + j) // 2
        r, c = mid // col, mid % col
        if matrix[r][c] == target: return True
        elif matrix[r][c] < target: i = mid + 1
        else: j = mid - 1
    return False
```

### [Leetcode 240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
> Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
```
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
```

**Solution:** Search from top-right, compare current value with target. Based on equality, update `i` and `j`.
```python
def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]: return False
    
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target: return True
        elif matrix[i][j] < target: i += 1
        else: j -= 1
    return False
```
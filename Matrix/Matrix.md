# Matrix

## Traversal

### Top-Left to Bottom-Right Traversal

#### [Leetcode 62. Unique Paths](https://leetcode.com/problems/unique-paths/)
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
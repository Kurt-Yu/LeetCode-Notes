# Matrix Related DP Problems

## [Leetcode 64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
> Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

The solution is pretty straightforward:
````Python
def minPathSum(self, grid):
    if not grid or not grid[0]: return 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0: grid[i][j] += grid[i][j - 1] if j > 0 else 0
            elif j == 0: grid[i][j] += grid[i - 1][j] if i > 0 else 0
            else: grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]) 
    return grid[-1][-1]
```
# Flood Fill Algorithm

Flood Fill algorithm is often used to solve this kind of questions: Given a 2d grid map of `'1's` (land) and `'0's` (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

The idea is that, start from a cell that has a `1` in it, modify it to `0`, then recursively call floodfill function to check its surrounding cells, as long as the adjacent cells are within the matrix boundary.

## Basic Template

### [Leetcode 200](https://leetcode.com/problems/number-of-islands/)
```python
def numIslands(self, grid: List[List[str]]) -> int:
    def floodfill(i, j):
        if grid[i][j] == '1':
            grid[i][j] = '0'
            if i > 0:
                floodfill(i - 1, j)
            if i < len(grid) - 1:
                floodfill(i + 1, j)
            if j > 0:
                floodfill(i, j - 1)
            if j < len(grid[0]) - 1:
                floodfill(i, j + 1)
                
    
    
    if not grid or not grid[0]: return 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                res += 1
                floodfill(i, j)
    return res
```
Anther short but a little bit expensive way is to use `map`:

```python
def numIslands(self, grid: List[List[str]]) -> int:
    def helper(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            list(map(helper, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            return 1
        return 0
    return sum(helper(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
```
Notice that in `python 3`, `map` function just returns a map object, instead of a iterable. If we want to actually evaluate the function, we need add a `list` in front of it. Though this might take more runtime.


Flood Fill with helper `visited` to store information that whether is cell is visited or not:

### [Leetcode 733](https://leetcode.com/problems/flood-fill/)
```python
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def helper(i, j, target):
        if image[i][j] == target and visited[i][j] == 0:
            image[i][j] = newColor
            visited[i][j] = 1
            if i > 0:
                helper(i - 1, j, target)
            if i < len(image) - 1:
                helper(i + 1, j, target)
            if j > 0:
                helper(i, j - 1, target)
            if j < len(image[0]) - 1:
                helper(i, j + 1, target)
    
    if not image: return []
    visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    helper(sr, sc, image[sr][sc])
    return image
```

Note that since the test might have some edge case like this: 
```python
iamge = [[0,0,0],[0,1,1]]
sr = 1, sc = 1, newColor = 1
```
In this case, the `visited` matrix helps us keep track of nodes, and prevent us from recursion over and over again.



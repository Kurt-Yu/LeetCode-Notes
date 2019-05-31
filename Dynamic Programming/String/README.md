# String Related DP Problems

+ [Leetcode 583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

## 583. Delete Operation for Two Strings
**Idea**: The idea is the same as *Longest Common Subsequence* problem, use a 2d array and dynamically expend the longest substring so far.

```python
def minDistance(self, word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    res = 0
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j] + (word1[j] == word2[i]))
    return m + n - dp[n][m] * 2
```




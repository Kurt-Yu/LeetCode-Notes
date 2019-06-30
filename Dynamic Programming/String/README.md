# String Related DP Problems

## [Leetcode 139. Word Break](https://leetcode.com/problems/word-break/)
> Given a non-empty string `s` and a dictionary `wordDict` containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Solution: `dp[i]` denotes whether `s[:i]` can be built.
```python
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    dp = [True]
    for i in range(1, len(s) + 1):
        dp.append(any(dp[j] and s[j:i] in words for j in range(i)))
    return dp[-1]
```

## [Leetcode 583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

**Solution**: The idea is the same as *Longest Common Subsequence* problem, use a 2d array and dynamically expend the longest substring so far.

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




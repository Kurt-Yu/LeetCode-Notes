# Palindromic Related DP Problems

This article contains Palindromic related problems, they can typically be solved by recursivly find the `max or min` values of the sub-problems. Below is a good example.

## [Leetcode 5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
> Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

**Method 1:** Non-DP Approach
```python
def longestPalindrome(self, S: str) -> str:
    res = ""
    for i in range(len(S)):
        res = max(self.helper(S, i, i), self.helper(S, i, i + 1), res, key = len)
    return res
        
def helper(self, S, left, right):
    while left >= 0 and right < len(S) and S[left] == S[right]:
        left, right = left - 1, right + 1
    return S[left + 1:right]
```

The whole idea is that, we start from some index `i` and then treat it as middle of some palindromic string, extend to both ends to find the longest one. Notice here we used a python trick: `res = max(....,  key = len)`, we give `key = len` as a parameter to `max` function and we are telling `max` to compare the length of parameters. **Time Complexity: O(n)**.

**Method 2:** DP Approach

```python
def longestPalindrome(self, S: str) -> str:
    res = ""
    dp = [[False] * len(S) for _ in range(len(S))]
    for i in range(len(S) - 1, -1, -1):
        for j in range(i, len(S)):
            dp[i][j] = S[i] == S[j] and (j - i < 3 or dp[i + 1][j - 1])
            
            if dp[i][j] and j - i + 1 > len(res):
                res = S[i:j + 1]
    return res
```

The basic idea is that `dp(i, j)` represents whether sub-string `S[i:j + 1]` is a palindromic or not. We can derive the following recursive relation: `dp(i, j) = dp(i + 1, j - 1) and S[i] == S[j]`. 

## [Leetcode 516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
> Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

**Solution:** The idea is essentially the same as the above question. Instead store `True` or `False` in `dp` table to present weither string `s[i:j + 1]` is a palindromic, we store the longest length of the palindromic inside substring `s[i:j + 1]`.

```Python
def longestPalindromeSubseq(self, s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]
    res = 0
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if i == j: dp[i][j] = 1
            elif j - i == 1: dp[i][j] = 2 if s[i] == s[j] else 1
            elif s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1] + 2
            else: dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
            
            res = max(res, dp[i][j])
    return res
```

## [Leetcode 647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
> Given a string, your task is to count how many palindromic substrings in this string.

Solution: this problem is essentially the same as the above one. We count the number of palindromic instead of storing the longest one.
```python
def countSubstrings(self, S: str) -> int:
    res = 0
    dp = [[False] * len(S) for _ in range(len(S))]
    for i in range(len(S) - 1, -1, -1):
        for j in range(i, len(S)):
            dp[i][j] = S[i] == S[j] and (j - i < 3 or dp[i + 1][j - 1])
            if dp[i][j]: res += 1
    return res
```


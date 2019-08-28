# Math Related DP Problems

## [Leetcode 279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)
> Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

**Solution:** `dp[n] = min(dp[n - i * i] + 1), where n - i * i >= 0 && i >= 1`. The idea is adapted from [this post](https://leetcode.com/problems/perfect-squares/discuss/71495/An-easy-understanding-DP-solution-in-Java).

```
dp[0] = 0 
dp[1] = dp[0]+1 = 1
dp[2] = dp[1]+1 = 2
dp[3] = dp[2]+1 = 3
dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 } 
      = Min{ dp[3]+1, dp[0]+1 } 
      = 1				
dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 } 
      = Min{ dp[4]+1, dp[1]+1 } 
      = 2
						.
						.
						.
dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 } 
       = Min{ dp[12]+1, dp[9]+1, dp[4]+1 } 
       = 2
						.
						.
						.
dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1
```

```Python
def numSquares(self, N):
    dp = [0] * (N + 1)
    for n in range(1, N + 1):
        i = 1
        res = float('inf')
        while i * i <= n:
            res = min(res, dp[n - i * i] + 1)
            i += 1
        dp[n] = res
    return dp[-1]
```
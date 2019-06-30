# Dynamic Problems About Array

This article includes some typical dynamic problems that associated with arrays, this kind of questions often requires us to iterate through and return some optimal value.

This particular problem and most of others can be approached using the following sequence:

+ Find recursive relation
+ Recursive (top-down)
+ Recursive + memo (top-down)
+ Iterative + memo (bottom-up)
+ Iterative + N variables (bottom-up)

## [Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
> Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Solution: `dp[i]` denotes the max sum ending at index `i`. If `dp[i - 1]` is negative, then there is no point adding `nums[i]` to it. We can just take `nums[i]` and consider it as the starting point. Otherwise, we add them together, and the result would be the current max value.

Recursive relation: `dp[i] = max(dp[i - 1] + nums[i], nums[i])`

```python
# Method 1:
def maxSubArray(self, nums: List[int]) -> int:
    if not nums: return 0
    dp = [0] * len(nums)
    dp[0] = res = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i] + dp[i - 1], nums[i])
        res = max(res, dp[i])
    return res

# Method 2: Notice that we don't need to keep track of dp[i].
# We can just do the same process on the original list `nums`
# which has a space complexity of O(1):

def maxSubArray(self, nums: List[int]) -> int:
    if not nums: return 0

    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)
```

## [Leetcode 198. House Robber](https://leetcode.com/problems/house-robber/)
The recursive relation in this problem is: 

`rob(i) = max(rob(i - 2) + currValue, rob(i - 1)`

```python
# Method 1: naive recursive solution, won't pass
def rob(self, nums: List[int]) -> int:
    def helper(nums, i):
        if i < 0: return 0
        return max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
    return helper(nums, len(nums) - 1)


# Method 2: recursive solution with memo (top-up)
# Space & Time: O(n)
def rob(self, nums: List[int]) -> int:
    memo = {}
    def helper(nums, i):
        if i < 0: return 0
        if i in memo: return memo[i]
        res = max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
        memo[i] = res
        return res
    
    return helper(nums, len(nums) - 1)


# Method 2: recursive solution with memo (bottom-up)
# Space & Time: O(n)
def rob(self, nums: List[int]) -> int:
    if not nums: return 0
    memo = [0] * (len(nums) + 1)
    memo[1] = nums[0]
    for i in range(2, len(nums) + 1):
        memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])
    return memo[-1]


# Method 3: Notice that only the last two variables are useful to us
# Thus we can throw away previous variable to save space
# `temp`: temp[0]: value when we don't rob, temp[1]: value when we rob
# Time: O(n), Space: O(1)
def rob(self, nums: List[int]) -> int:
    temp = [0, 0]
    for n in nums:
        temp = [max(temp), n + temp[0]]
    return max(temp)
```
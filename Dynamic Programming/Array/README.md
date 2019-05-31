# Dynamic Problems About Array

This article includes some typical dynamic problems that associated with arrays, this kind of questions often requires us to iterate through and return some optimal value.

This particular problem and most of others can be approached using the following sequence:

+ Find recursive relation
+ Recursive (top-down)
+ Recursive + memo (top-down)
+ Iterative + memo (bottom-up)
+ Iterative + N variables (bottom-up)

## [198. House Robber](https://leetcode.com/problems/house-robber/)
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
# Space complexity: O(n) because of recursive stack
# Time complexity: O(n)
def rob(self, nums: List[int]) -> int:
    memo = {}
    def helper(nums, i):
        if i < 0: return 0
        if i in memo: return memo[i]
        res = max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
        memo[i] = res
        return res
    
    return helper(nums, len(nums) - 1)



```
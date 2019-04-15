"""
Leetcode 209: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
def minSubArrayLen(self, s, nums):
    res = len(nums) + 1
    i = 0
    total = 0
    for j, n in enumerate(nums):
        total += n
        if total >= s:
            while total - nums[i] >= s:
                total -= nums[i]
                i += 1
            res = min(res, j - i + 1)
    return res if res != len(nums) + 1 else 0
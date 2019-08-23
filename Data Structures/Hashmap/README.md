# Hashmap / Dict

This article contains some typical problems that can be solve by hashmap. It is a useful data structure when we want to store previous states of some key.

## [Leetcode 560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
> Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

**Solution:** Keep track of the current sum `total`, if their exist some value `total - k` 
```python
def subarraySum(self, nums: List[int], k: int) -> int:
    count = {0:1}
    res, total = 0, 0
    for n in nums:
        total += n
        res += count.get(total - k, 0)
        count[total] = count.get(total, 0) + 1
    return res
```
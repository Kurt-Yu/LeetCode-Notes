# Python Tricks

## Higher Order Functions
Since lots of higher order functions have been moved to `functools` module, we need to `import functools` before we actual use any of them.

### `reduce()`: [Leetcode 136. Single Number](https://leetcode.com/problems/single-number/)

>Given a non-empty array of integers, every element appears twice except for one. Find that single one.

```python
def singleNumber(self, nums):
    import functools
    return reduce(lambda x, y : x ^ y, nums)
```

### `map()`: 

Freauently Usage: `list(map(int, input().split()))`

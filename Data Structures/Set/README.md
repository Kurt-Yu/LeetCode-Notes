# Set

Set is a fairly easy data structure. We often use it when we want to decrease the time complexity of `search` operation, since searching an element in a set only takes `O(1)` time. Set is unordered with no duplicates, and each element appears only once. It is a good choose when we want to count the number of distinct elements in some collection.

## [Leetcode 771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
```python
def numJewelsInStones(self, J: str, S: str) -> int:
    J = set(J)
    res = 0
    for s in S:
        if s in J: res += 1
    return res
```


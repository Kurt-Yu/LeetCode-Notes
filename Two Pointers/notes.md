# Two Pointers
Two Pointers is a typical algorithms design technique. It is used when we want to manipulate or do some operation on a already sorted list (or doubly linked list), which can dramatically decrease the running time. 

Here is a typical problem that can be solved using two pointers: Given an array of integers `A` sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

If we simply calculate the square of each number, then sort the list, that would be `O(nlogn)` time complexity. By comparing the left and right element of list, we can reduce the time complexity to `O(n)`

[Leetcode 977](https://leetcode.com/problems/squares-of-a-sorted-array/)
```python
def sortedSquares(self, A: List[int]) -> List[int]:
    res = []
    left, right = 0, len(A) - 1
    while left <= right:
        l, r = abs(A[left]), abs(A[right])
        if l < r:
            res.insert(0, r * r)
            right -= 1
        else:
            res.insert(0, l * l)
            left += 1
    return res
```



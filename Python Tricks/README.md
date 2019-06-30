# Python Tricks

## Higher Order Functions
Since lots of higher order functions have been moved to `functools` module, we need to `import functools` before we actual use any of them.

### `reduce()`: [Leetcode 136. Single Number](https://leetcode.com/problems/single-number/)

> Given a non-empty array of integers, every element appears twice except for one. Find that single one.

```python
def singleNumber(self, nums):
    import functools
    return reduce(lambda x, y : x ^ y, nums)
```

## Data Structures
### [heapq](https://docs.python.org/3.0/library/heapq.html)

> This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

> Heaps are arrays for which `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all `k`, counting elements from zero. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that `heap[0]` is always its **smallest** element.

Frequently Usage:
```python
import heapq

heapq.heapify(x)              # Transform x into a heap, in-place, linear time
heapq.heappop(heap)           # pop and return the smallest element item from heap
heapq.heappush(heap, item)    # push the item into heap
heapq.heapreplace(heap, item) # pop and return the smallest item from heap, and also push the new item
```
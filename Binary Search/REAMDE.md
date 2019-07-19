# Binary Search

Binary Search usually used to solve this kind of question: Given a sorted (in ascending order) integer array nums of `n` elements and a `target` value, write a function to search target in nums. If target exists, then return its `index`, otherwise return `-1`.

The idea is simple: check the middle element of array and compare it with target, is target is smaller, search the left half, if target is larger, then search the right half. If equal, which means we found the target, then just return the index. If target doesn't exist in array, we return -1.

## Basic Template
### [Leetcode 704. Binary Search](https://leetcode.com/problems/binary-search/):
```python
# iterative solution (48 ms):

def search(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1
```

Note that the condition for while loop is `<=` rather than `<`. Consider the case with only one element, say `nums = [5]`. We need `<=` to ensure the while loop is actaully executed.

```python
# recursive solution (144 ms):

def search(self, nums: List[int], target: int) -> int:
    def helper(low, high):
        if low > high: return -1
        mid = (low + high) // 2
        if nums[mid] > target:
            return helper(low, high - 1)
        elif nums[mid] < target:
            return helper(low + 1, high)
        else:
            return mid
    return helper(0, len(nums) - 1)
```

## Variants
### [Leetcode 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/): Find First and Last Position of Element in Sorted Array

We just need to change the above template a little bit, since we ar looking for first and last position of target, then just do two binary search.

```python 
def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchLeft():
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]: high = mid - 1
            else: low = mid + 1
        return left
    
    def searchRight():
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target >= nums[mid]: low = mid + 1
            else: high = mid - 1
        return right
    
    left, right = searchLeft(), searchRight()
    return [left, right] if left <= right else [-1, -1]
``` 

### [Leetcode 981](https://leetcode.com/problems/time-based-key-value-store/): Time Based Key-Value Store

One thing that worth mention is that python has a build-in library for dealing with sorted array (internally implemented using binary search) called `bisect`.

```python
import bisect
class TimeMap:

    def __init__(self):
        self.kv = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv: return ''
        idx = bisect.bisect_right(self.kv[key], (timestamp, '{'))
        return '' if idx == 0 else self.kv[key][idx-1][1]
```

## Find Peek Element

### [Leetcode 852](https://leetcode.com/problems/peak-index-in-a-mountain-array/): Peak Index in a Mountain Array

`O(N)` solution: find the index of largest element:
```python
def peakIndexInMountainArray(self, A: List[int]) -> int:
    return A.index(max(A))
```

`O(logn)` solution: using binary search:
```python
def peakIndexInMountainArray(self, A: List[int]) -> int:
    low, high = 0, len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < A[mid + 1]:
            low = mid + 1
        elif A[mid] < A[mid - 1]:
            high = mid - 1
        else: return mid
```

### [Leetcode 162](https://leetcode.com/problems/find-peak-element/): Find Peak Element

```python
def findPeakElement(self, nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
```

## Rotated Array

### [Leetcode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/): Search in Rotated Sorted Array


```python
def search(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        
        if nums[mid] < nums[high]:
            if nums[mid] < target <= nums[high]: low = mid + 1
            else: high = mid - 1
        else:
            if nums[low] <= target < nums[mid]: high = mid - 1
            else: low = mid + 1
    return -1
```

### [Leetcode 81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/): Search in Rotated Sorted Array II

Almost the same as last question, now we had duplicates in array, so we need to get rid of the duplicates by a `while` loop, see line 6-7.

```python
def search(self, nums: List[int], target: int) -> bool:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return True
        while low < mid and nums[low] == nums[mid]: # tricky part
            low += 1
            
        # the first half is ordered
        if nums[low] <= nums[mid]:
            # target is in the first half
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # the second half is ordered
        else:
            # target is in the second half
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False
```

### [Leetcode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/): Find Minimum in Rotated Sorted Array

```python
def findMin(self, nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1
    return nums[low]
```

### [Leetcode 154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/): Find Minimum in Rotated Sorted Array II

```python
def findMin(self, nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            high -= 1
    return nums[low]
```

## Search 2d Matrix

### [Leetcode 74](https://leetcode.com/problems/search-a-2d-matrix/): Search a 2D Matrix

When searching in a 2d matrix, the idea is that: not treat it as a matrix, instead, treat it as a "large" sorted list. The index can be easily calculated with `//` and `%`.

```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix: return False
    row, col = len(matrix), len(matrix[0])
    low, high = 0, row * col - 1
    while low <= high:
        mid = (low + high) // 2
        i, j = mid // col, mid % col
        if target < matrix[i][j]:
            high = mid - 1
        elif target > matrix[i][j]:
            low = mid + 1
        else: return True
    return False
```

### [Leetcode 240](https://leetcode.com/problems/search-a-2d-matrix-ii/): Search a 2D Matrix II

To be precise, this problem is not a binary search problem. I put it here just because it's the follow question of last one. The idea is this: we start from the right top corner, if target is smaller than current element, then we search for current row. If not, then update row index to next level.

```python
def searchMatrix(self, matrix, target):
    if not matrix: return False
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target: return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return False
```
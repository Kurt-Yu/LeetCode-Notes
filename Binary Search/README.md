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
### [Leetcode 34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

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

### [Leetcode 981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

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

### [Leetcode 852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

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

### [Leetcode 162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

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

### [Leetcode 33 Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. You are given a target value to search. If found in the array return its index, otherwise return -1.

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

### [Leetcode 81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

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

### [Leetcode 153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

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

### [Leetcode 154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

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

### [Leetcode 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

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

### [Leetcode 240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

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

## Advanced problems That Uses Binary Search

### [Leetcode 4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
> There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

> You may assume nums1 and nums2 cannot be both empty.

**Solution:** For you reference, this solution is adpated from [this post](https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation).

```python
def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    
    
    imin, imax = 0, m
    half_len = (n + m + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        
        if i < m and B[j-1] > A[i]:
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            imax = i - 1
        else:
            max_of_left, min_of_right = 0, 0
            
            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2
```
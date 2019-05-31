# Sorting Algorithms

## QuickSort

QuickSort with additional memory:
```python
def quicksort(nums):
    if len(nums) > 1:
        smaller, equal, greater = [], [], []
        pivot = nums[0]
        for n in nums:
            if n == pivot: equal.append(n)
            elif n < pivot: smaller.append(n)
            else: greater.append(n)
        return quicksort(smaller) + pivot + quicksort(greater)
    else:
        return nums
```

Another concise and elegant way to implement it:
```python
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        return quicksort([x for x in nums[1:] if x < nums[0]]) + nums[0] + quicksort([x for x in nums[1:] if x >= nums[0]])
```

*Just For Fun: Write QuickSort in Haskell:*

```haskell
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = 
    let smallerSorted = quicksort [a | a <- xs, a <= x]
        biggerSorted = quicksort [a | a <- xs, a > x]
    in smallerSorted ++ [a] ++ biggerSorted
```

Quicksort without additiona memory (in-place):

```python
def partition(nums, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if nums[i] <= nums[start]:
            pivot += 1
            nums[pivot], nums[i] = nums[i], nums[pivot]
    nums[start], nums[pivot] = nums[pivot], nums[start]
    return pivot

def helper(nums, start, end):
    if start >= end: return
    pivot = partition(nums, start, end)
    helper(nums, start, pivot - 1)
    helper(nums, pivot + 1, end)

def quicksort(nums):
    return helper(nums, 0, len(nums) - 1)
```

## Selection Sort
**Idea**: Find the minimun value in the rest of array each iteration, and swap the current minimun to the start.

Time complexity: `O(n^2)`, Space complexity: `O(1)`
```python
def selection_sort(nums):
    for i in range(len(nums)):
        curr = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[curr]:
                curr = j
        nums[curr], nums[i] = nums[i], nums[curr]
```

## Insertion Sort
**Idea**: Maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.

```python
def insertion_sort(nums):
   for i in range(1, len(nums)):
        curr = nums[i]
        temp = i

        while temp > 0 and nums[temp - 1] > curr:
            nums[temp] = nums[temp - 1]
            temp -= 1

        nums[temp] = curr
```

## Merge Sort

```python
def merge_sort(nums):
    if len(nums) < 2: return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    while left and right:
        if left[0] > right[0]: res.append(right.pop(0))
        else: res.append(left.pop(0))
    res.extend(left + right)

    return res
```
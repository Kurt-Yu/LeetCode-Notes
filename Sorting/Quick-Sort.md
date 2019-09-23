# QuickSort

**QuickSort with additional memory:**
```python
def quicksort(nums):
    if len(nums) <= 1: return nums

    smaller, equal, greater = [], [], []
    pivot = nums[0]
    for n in nums:
        if n == pivot: equal.append(n)
        elif n < pivot: smaller.append(n)
        else: greater.append(n)
    return quicksort(smaller) + pivot + quicksort(greater)
```

**Another concise and elegant way to implement it:**
```python
def quicksort(nums):
    if len(nums) <= 1: return nums

    return quicksort([x for x in nums[1:] if x < nums[0]]) + nums[0] + quicksort([x for x in nums[1:] if x >= nums[0]])
```

**Quicksort without additiona memory (in-place):**
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
    helper(nums, 0, len(nums) - 1)
    print(nums)    # since this is a in-place algorithms, it does not return anything
```

*Just For Fun: Implement QuickSort in Haskell:*
```haskell
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = 
    let smallerSorted = quicksort [a | a <- xs, a <= x]
        biggerSorted = quicksort [a | a <- xs, a > x]
    in smallerSorted ++ [a] ++ biggerSorted
```

## QuickSort in Action

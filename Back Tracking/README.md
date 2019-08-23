# Backtracking
Backtracking algorithm is often used together with recursive, mainly dealing with list or trees. Consider the case where we do recursive call on a given binary tree, and finally it reaches the leave node (or `None` node). We do some operation on this node, then the current recursive stack exits, followed by the outer recursive call. This kind of approach is typicallt called `backtracking`, because we start from base case then track from backwards.

+ [Leetcode 78. Subsets](https://leetcode.com/problems/subsets/)
+ [Leetcode 90. Subsets II](https://leetcode.com/problems/subsets-ii/)
+ [Leetcode 46. Permutations](https://leetcode.com/problems/permutations/)


## [Leetcode 78. Subsets](https://leetcode.com/problems/subsets/)
Given a set of distinct integers, nums, return all possible subsets (the power set).
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(res, [], nums, 0)
        return res
    
    def backtrack(self, res, temp, nums, start):
        res.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(res, temp, nums, i + 1)
            temp.pop()
```

Another approach: Iterative solution

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in range(len(nums)):
        res += [item + [nums[i]] for item in res]
    return res
```

## Leetcode 90. Subsets II 
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(res, [], nums, 0)
        return res
        
        
    def backtrack(self, res, temp, nums, start):
        res.append(temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1] : continue
            temp.append(nums[i])
            self.backtrack(res, temp, nums, i + 1)
            temp.pop()
```

## Leetcode 46. Permutations
Given a collection of distinct integers, return all possible permutations.
```python

```


## Leetcode Problems
[Leetcode 336](https://leetcode.com/problems/find-leaves-of-binary-tree/)
```python
def findLeaves(self, root: TreeNode) -> List[List[int]]:
    def helper(res, root):
        if not root: return -1
        left, right = helper(res, root.left), helper(res, root.right)
        level = max(left, right) + 1
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        root.left, root.right = None, None
        return level
    res = []
    helper(res, root)
    return res
```

Notice that when the helper function finishes, we need to set `root.left` and `root.right` to `None`. Otherwise the function does not terminate., will loop over and over again. That line of code is a exit condition.

## 
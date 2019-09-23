# A Series of Back Tracking Problems

+ [Leetcode 78. Subsets](https://leetcode.com/problems/subsets/)
+ [Leetcode 90. Subsets II](https://leetcode.com/problems/subsets-ii/)
+ [Leetcode 46. Permutations](https://leetcode.com/problems/permutations/)
+ [Leetcode 47. Permutations II](https://leetcode.com/problems/permutations-ii/)
+ [Leetcode 39. Combination Sum](https://leetcode.com/problems/combination-sum/)
+ [Leetcode 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
+ [Leetcode 131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

## [Leetcode 78. Subsets](https://leetcode.com/problems/subsets/)
> Given a set of distinct integers, nums, return all possible subsets (the power set).

```Python
def subsets(self, nums):
    res = []
    self.backtracking(res, [], nums, 0)
    return res

def backtracking(self, res, temp, nums, start):
    res.append(temp[:])
    for i in range(start, len(nums)):
        temp.append(nums[i])
        self.backtracking(res, temp, nums, i + 1)
        temp.pop()
```

## [Leetcode 90. Subsets II](https://leetcode.com/problems/subsets-ii/)
> Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

```Python
def subsetsWithDup(self, nums):
    res = []
    nums.sort()
    self.backtracking(res, [], nums, 0)
    return res

def backtracking(self, res, temp, nums, start):
    res.append(temp[:])
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]: continue
        temp.append(nums[i])
        self.backtracking(res, temp, nums, i + 1)
        temp.pop()
```

## [Leetcode 46. Permutations](https://leetcode.com/problems/permutations/)
> Given a collection of distinct integers, return all possible permutations.

```Python
def permute(self, nums):
    res = []
    self.backtracking(res, [], nums)
    return res

def backtracking(self, res, temp, nums):
    if len(temp) == len(nums): 
        res.append(temp[:])
        return
    for i in range(len(nums)):
        if nums[i] in temp: continue
        temp.append(nums[i])
        self.backtracking(res, temp, nums)
        temp.pop()
```

## [Leetcode 47. Permutations II](https://leetcode.com/problems/permutations-ii/)
> Given a collection of numbers that might contain duplicates, return all possible unique permutations.

```python
def permuteUnique(self, nums):
    res = []
    nums.sort()
    used = [False] * len(nums)
    self.backtracking(res, [], nums, used)
    return res

def backtracking(self, res, temp, nums, used):
    if len(temp) == len(nums):
        res.append(temp[:])
        return
    
    for i in range(len(nums)):
        if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]): continue
        used[i] = True
        temp.append(nums[i])
        self.backtracking(res, temp, nums, used)
        used[i] = False
        temp.pop()
```

## [Leetcode 39. Combination Sum](https://leetcode.com/problems/combination-sum/)
> Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

> The same repeated number may be chosen from candidates unlimited number of times.

```Python
def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.backtracking(res, [], candidates, target, 0)
    return res
    
def backtracking(self, res, temp, candidates, target, start):
    if target < 0: return
    if target == 0: 
        res.append(temp[:])
        return

    for i in range(start, len(candidates)):
        temp.append(candidates[i])
        self.backtracking(res, temp, candidates, target - candidates[i], i) # not i + 1 because we can reuse same elements
        temp.pop()
```

## [Leetcode 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
> Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

> Each number in candidates may only be used once in the combination.

```Python
def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()
    self.backtracking(res, [], candidates, target, 0)
    return res

def backtracking(self, res, temp, candidates, target, start):
    if target < 0: return
    if target == 0:
        res.append(temp[:])
        return
    
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]: continue
        temp.append(candidates[i])
        self.backtracking(res, temp, candidates, target - candidates[i], i + 1)
        temp.pop()
```

## [Leetcode 131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
> Given a string s, partition s such that every substring of the partition is a palindrome.

> Return all possible palindrome partitioning of s.

```Python
def partition(self, s):
    res = []
    self.backtracking(res, [], s, 0)
    return res
    
    
def backtracking(self, res, temp, s, start):
    if start == len(s):
        res.append(temp[:])
        return
    
    for i in range(start, len(s)):
        if self.is_palindrome(s, start, i):
            temp.append(s[start:i + 1])
            self.backtracking(res, temp, s, i + 1)
            temp.pop()
        
def is_palindrome(self, s, i, j):
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True
```
# Path Sum Problems

+ [Leetcode 112. Path Sum](https://leetcode.com/problems/path-sum/)
+ [Leetcode 113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
+ [Leetcode 437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
+ [Leetcode 666. Path Sum IV](https://leetcode.com/problems/path-sum-iv/)
+ [Leetcode 124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
+ [Leetcode 687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
+ [Leetcode 543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

## Basic Template

Return all root to leaf paths in a binary tree in the form of a list (Ex. ["1->2->5", "1->3"]).

**Note:** This template is really powerful and extremely useful. Once you get used to it, it will help to solve lots of similar problems. You will see that below in `Path Sum II`, we used this template.
```python
def allPaths(root):
    if not root: return []
    if not root.left and not root.right:
        return [str(root.val)]
    return [str(root.val) + '->'+ l for l in allPaths(root.right) + allPaths(root.left)]
```

## [Leetcode 112. Path Sum](https://leetcode.com/problems/path-sum/)
> Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

```python
# Method 1: Recursive
def hasPathSum(self, root, target):
    if not root: return False
    if not root.left and not root.right: return target == root.val
    return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)

# Method 2: BFS
def hasPathSum(self, root, target):
    if not root: return False
    
    stack = [(root, target)]
    while stack:
        node, target = stack.pop(0)
        if not node.left and not node.right and target == node.val: return True
        if node.left:
            stack.append((node.left, target - node.val))
        if node.right:
            stack.append((node.right, target - node.val))
    return False
```

## [Leetcode 113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
> Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

```python
# Method 1: Use the template above
def pathSum(self, root, target):
    if not root: return []
    if not root.left and not root.right and root.val == target:
        return [[root.val]]
    return [[root.val] + l for l in self.pathSum(root.left, target - root.val) + self.pathSum(root.right, target - root.val)]

# Method 2: BFS, slightly modification of the above code
def pathSum(self, root, target):
    if not root: return []

    stack = [(root, target, [root.val])]
    res = []
    while stack:
        node, target, temp = stack.pop(0)
        if not node.left and not node.right and target == node.val:
            res.append(temp)
        if node.left:
            stack.append((node.left, target - node.val, temp + [node.left.val]))
        if node.right:
            stack.append((node.right, target - node.val, temp + [node.right.val]))
    return res

# Method 3: DFS (pre-order) (recursive)

# You can see the original pre-order traversal code from traversal.md file
# and discover how we can use the template to solve other problems
def pathSum(self, root, target):
    res = []
    
    def helper(node, temp, target):
        if node: 
            if not node.left and not node.right and node.val == target:
                temp.append(node.val)
                res.append(temp)
            helper(node.left, temp + [node.val], target - node.val)
            helper(node.right, temp + [node.val], target - node.val)
    
    helper(root, [], target)
    return res
```


## [Leetcode 437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
> You are given a binary tree in which each node contains an integer value.

> Find the number of paths that sum to a given value.

> The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

This solution is adapted from [this post](https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)).
```python
def pathSum(self, root, target):
    prefix = {0:1}
    self.res = 0
    
    def dfs(node, target, acc):
        if not node: return None
        
        acc += node.val
        self.res += prefix.get(acc - target, 0)
        prefix[acc] = prefix.get(acc, 0) + 1
        
        dfs(node.left, target, acc)
        dfs(node.right, target, acc)
        
        prefix[acc] -= 1
    
    dfs(root, target, 0)
    return self.res
```

## [Leetcode 666. Path Sum IV](https://leetcode.com/problems/path-sum-iv/)
> If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

```
For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
```

> Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

```Python
# BFS
def pathSum(self, nums):
    if not nums: return 0
    
    root = nums.pop(0)
    stack = [(root, [root % 10])]
    temp = {node//10 : node for node in nums}
    res = 0
    
    while stack:
        node, path = stack.pop(0)
        level, pos = node // 100, (node // 10) % 10
        next_level, left, right = level + 1, pos * 2 - 1, pos * 2
        
        left += next_level * 10
        right += next_level * 10
        if left in temp:
            stack.append((temp[left], path + [temp[left] % 10]))
        if right in temp:
            stack.append((temp[right], path + [temp[right] % 10]))
    
        if (left not in temp) and (right not in temp):
            res += sum(path)
    return res
```


## [Leetcode 124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
> Given a non-empty binary tree, find the maximum path sum.

> For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

This solution is adpated from [this post](https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39775/Accepted-short-solution-in-Java).

```Python
class Solution(object):
    def maxPathSum(self, root):
        self.res = float('-inf')
        
        def helper(node):
            if not node: return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val

        helper(root)

        return self.res
```

**Problems below this line doesn't involve calculating `Path Sum`. But I still put them here because they used almost the same ideas as above problems. Hope you could find some similarities between all of those questions. Enjoy :)**

## [Leetcode 687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
> Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

> The length of path between two nodes is represented by the number of edges between them.

**Solution:** This problem requires us find a longest path such that all nodes in this path have the same value. And it does not have to pass through the root, which remainds us of the `Path Sum IV` problem. In `Path Sum IV` (please see above), we used a global variable `self.res`. We udpate the result as we recursively call our helper function. In the recursive call, what we have to do is simply compare parent node's val with current node's val. And determine the return result based on there equality.

```python
class Solution(object):
    def longestUnivaluePath(self, root):
        if not root: return 0
        self.res = 0
        
        def get_length(node, val):
            if not node: return 0
            left = get_length(node.left, node.val)
            right = get_length(node.right, node.val)
            self.res = max(self.res, left + right)
            return max(left, right) + 1 if node.val == val else 0
        
        get_length(root, root.val)

        return self.res
```

## [Leetcode 543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
> Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

**Solution:** Almost the same code as last quesion, with slightly modification.
```Python
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.res = 0
        
        def get_diameter(node):
            if not node: return 0
            left = get_diameter(node.left)
            right = get_diameter(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        
        get_diameter(root)
        
        return self.res
```
# Backtracking
Backtracking algorithm is often used together with recursive, mainly dealing with list or trees. Consider the case where we do recursive call on a given binary tree, and finally it reaches the leave node (or `None` node). We do some operation on this node, then the current recursive stack exits, followed by the outer recursive call. This kind of approach is typicallt called `backtracking`, because we start from base case then track from backwards.

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

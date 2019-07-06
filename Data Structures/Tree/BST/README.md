# Binary Search Tree

This article is about BST. It is a special kind of binary tree such that for each node, the value in this node is greater than all the left sub-nodes and smaller than all the right sub-nodes. The problems related to BST can often be solved by recusion.

## [Leetcode 98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
> Given a binary tree, determine if it is a valid binary search tree (BST).

```python
# Method 1: using recursion
# Time Complexity: O(n), Space Complexity: O(n), because of the recusive stack
def isValidBST(self, root: TreeNode, left = float('-inf'), right = float('inf')) -> bool:
    if not root: return True
    return left < root.val < right and self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)

# Method 2: using inorder travesal
# Time & Space Complexity
def isValidBST(self, root):
    inorder = []
    def helper(node):
        if node:
            helper(node.left)
            inorder.append(node.val)
            helper(node.right)
    helper(root)
    
    temp = float('-inf')
    for n in inorder:
        if n <= temp: return False
        temp = n
    return True

# Method 3: Notice that we can reduce the space complexity by keep track of a temprary variable,
# for each step of inorder traversal, we just need to compare current value with temp
# there is no need to store the entire `inorder` array and do the check at last
def isValidBST(self, root):
    self.temp = float('-inf')
    self.res = True
    
    def helper(node):
        if node:
            helper(node.left)
            if node.val <= self.temp:
                self.res = False
            self.temp = node.val
            helper(node.right)
    helper(root)
    return self.res
```


# Recursive Patterns on Tree

Tree is a kind of data structure that has `root` and `left, right` children. Tree-like structures are typically manipulcated by recursive algorithms. But recursion isn't an easy thing to think about, cause sometimes it's hard to find the recursive relation. Thus this article is aiming to provide some recursive patterns. Hope we can sort things out.

## Ancestor

### [Leetcode 236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
> Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
```
Base Case: 
    1. If node is None, return None. 
    2. If node is p or q, there is no point continuing call the rest, just return node itself.
Recursive relation:
    Recursively call left and right child.
Return Value:
    If both left and right are not None, then we've found the ancestore, return this node.
    Otherwise, return the non-None value.
```

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root in (None, p, q): return root
    left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
    return root if left and right else left or right
```
# Tree Traversal

## DFS

```python
"""
Preorder Iterative
"""
def preorderIterative(self, root: TreeNode) -> List[int]:
    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            res.append(root.val)
            root = root.left
        else:
            node = stack.pop()
            root = node.right
    return res

"""
Inorder Iterative
"""
def inorderIterative(self, root: TreeNode) -> List[int]: 
    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
    return res

"""
Postorder Iterative
"""
def postorderIterative(self, root: TreeNode) -> List[int]:
    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            res.insert(0, root.val)
            root = root.right
        else:
            node = stack.pop()
            root = node.left
    return res


"""
Preorder recursive
"""
def preorderRecursive(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if root:
            res.append(root.val)
            helper(root.left)
            helper(root.right)
    helper(root)
    return res

"""
Inorder recursive
"""
def inorderRecursive(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if root:
            helper(root.left)
            res.append(root.val)
            helper(root.right)
    helper(root)
    return res

"""
Postorder recursive
"""
def postorderRecursive(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if root:
            helper(root.left)
            helper(root.right)
            res.append(root.val)
    helper(root)
    return res
```

## BFS

```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    
    res, stack = [], [root]
    while stack:
        res.append([node.val for node in stack])
        children = [child for node in stack for child in (node.left, node.right) if child]
        stack = children
    return res
```
# Tree Traversal

This article gives the stardard template for tree traversal methods: DFS (perorder, inorder, postorder) & BFS, both iterative and recursive. We will also discuss some related problems regards to tree tarversals.

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

## Variants

### [Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not inorder: return None
    i = inorder.index(preorder.pop(0))
    root = TreeNode(inorder[i])
    root.left = self.buildTree(preorder, inorder[:i])
    root.right = self.buildTree(preorder, inorder[i + 1:])
    return root
```

### [Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
```python
def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder: return None
    i = inorder.index(postorder.pop())
    root = TreeNode(inorder[i])
    root.right = self.buildTree(inorder[i + 1:], postorder)
    root.left = self.buildTree(inorder[:i], postorder)
    return root
```

## Other Problems that can be solved by DFS or BFS
### [Leetcode 17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
> Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

**Idea:** This is essentially an BFS problem. We starts from an empty string `''` (consider it as a root node for some tree), then for each digit, it has three or four digits assocaited with it (consider them as three or four children nodes of root). Once we have this tree-like model in our head, we could expand our string level by level.

```python
def letterCombinations(self, digits: str) -> List[str]:
    if not digits: return []
    
    mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    res = ['']
    for digit in digits:
        current = []
        for letter in mapping[digit]:
            for temp in res:
                current.append(temp + letter)
        res = current
    return res
```

### [Leetcode 114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
> Given a binary tree, flatten it to a linked list in-place.

**Idea:** Do a `reversed` postorder while updating current node. This is essentially build the whole tree from right-bottom-up.
```Python
def flatten(self, root: TreeNode) -> None:
    self.prev = None
    def postorder(node):
        if not node: return None
        postorder(node.right)
        postorder(node.left)
        node.right, node.left = self.prev, None
        self.prev = node
    postorder(root)
```
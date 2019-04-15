def pathSum(self, root, target):
    self.res = 0
    cache = {0:1}

    def helper(root, curr):
        if root is None:
            return

        curr += root.val
        old = curr - target

        self.res += cache.get(old, 0)
        cache[curr] = cache.get(curr, 0) + 1

        helper(root.left, curr)
        helper(root.right, curr)
        cache[curr] -= 1
        
    helper(root, 0)
    return self.res
# Min Stack

## [Leetcode 155. Min Stack](https://leetcode.com/problems/min-stack/)
> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
```

**Solution:** Push item along with the current min value to the top of stack. Notice that in the `push` function, we cannot use `if not val or x < val` as the if condition, since when `val = 0`, `not val => True`. We have to explictly write out `val == None`. 
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        val = self.getMin()
        if val == None or x < val:
            self.stack.append([x, x])
        else:
            self.stack.append([x, val])

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack: return None
        return self.stack[-1][1]
```
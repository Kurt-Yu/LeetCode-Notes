# Stack

This article includes some typical leetcode problems that uses the `stack` data strucutre.

## Algorithmatic Problems

### [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
```python
def dailyTemperatures(self, T):
    res = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)
    return res
```

### [Leetcode 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
Given a string containing just the characters `(, ), {, }, [, ]`, determine if the input string is valid.

```python
def isValid(self, S: str) -> bool:
    stack = []
    for s in S:
        if s in '([{':
            stack.append(s)
        else:
            if s == ')':
                if stack and stack[-1] == '(': stack.pop()
                else: return False
            elif s == ']':
                if stack and stack[-1] == '[': stack.pop()
                else: return False
            else:
                if stack and stack[-1] == '{': stack.pop()
                else: return False
    return len(stack) == 0
```

## Design Problems

### [Leetcode 155. Min Stack](https://leetcode.com/problems/min-stack/)
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x) -> None:
        currMin = self.getMin()
        if currMin == None or x < currMin:
            currMin = x
        self.stack.append((x, currMin));

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
```
# Stack

This article includes some typical leetcode problems that uses the `stack` data strucutre.

## [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
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

## []()
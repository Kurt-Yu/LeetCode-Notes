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

### [Leetcode 394. Decode String] (https://leetcode.com/problems/decode-string/)
> Given an encoded string, return its decoded string.

> The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

> You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

> Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

```cpp
class Solution {
public:
    string decodeString(string s) {
        stack<string> stack;
        for (const auto& c : s) {
            if (c == ']') {
                string temp = "";
                while (!stack.empty() && isalpha(stack.top()[0])) {
                    temp = stack.top() + temp;
                    stack.pop();
                }
                stack.pop(); // pop the '[' character off
                
                string base = "";
                while (!stack.empty() && isdigit(stack.top()[0])) {
                    base = stack.top() + base;
                    stack.pop();
                }
                
                string new_string = "";
                for (int i = 0; i < stoi(base); i++) new_string.append(temp);
                stack.push(new_string);
            } else {
                stack.push(string(1, c));
            }
        }
        
        string res = "";
        while (!stack.empty()) {
            res = stack.top() + res;
            stack.pop();
        }
        
        return res;
    }
};
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
        self.stack.append((x, currMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
```
# Sliding Window Algorithm 

This algorithm can be used to solve a wide range of problems. Below I share the template code. Reference can be found [here](https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem).

## Similar Questions
+ [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
+ [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
+ [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
+ [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
+ [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

## Template

This the template written in Python:

```python
# s is the source string, t is the target string
def solution(s: str, t: str):
    # init a list or int value to save the result according the question.
    if len(t) > len(s): return []
    res = []

    # create a dict to store the characters of target string
    d = collections.Counter(t)

    # maintain a counter to check whether match the target string
    size = len(d)
    i, j = 0, 0

    # the length of substring which matches the target string
    lenght = float('inf)

    while j < len(s):
        if s[j] in d:
            d[s[j]] -= 1 # plus or minus one
            if d[s[j]] == 0: size -= 1 # modify the counter according the requirement(different condition).
        j += 1

        # increase begin pointer to make it invalid/valid again
        while size == 0:
            if s[i] in d:
                d[s[i]] += 1  # plus or minus one
                if d[s[i]] > 0: size += 1 # modify the counter according the requirement(different condition).

            # save / update(min/max) the result if find a target*/
            #  result collections or result int value
        
            i += 1
    
    return res
```

## Using template to solve above questions

### [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
```python
def minWindow(self, s: str, t: str) -> str:
    if len(t) > len(s): return ""

    i, j = 0, 0
    d = collections.Counter(t)
    size = len(d)
    head = 0
    length = float('inf')
    
    while j < len(s):
        if s[j] in d:
            d[s[j]] -= 1
            if d[s[j]] == 0: size -= 1 
        j += 1
        
        while size == 0:
            if s[i] in d:
                d[s[i]] += 1
                if d[s[i]] > 0: size += 1
                
            if j - i < length:
                length = j - i
                head = i
            
            i += 1
    return s[head:head + length] if length != float('inf') else ""
```

### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    i = j = 0
    res = 0
    while j < len(s):
        if s[j] in seen:
            i = max(i, seen[s[j]] + 1)
        seen[s[j]] = j
        res = max(res, j - i + 1)
        j += 1
    return res
```

### [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
```python
"""
TODO
"""
```

### [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
```python
"""
TODO
"""
```


### [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
```python

```


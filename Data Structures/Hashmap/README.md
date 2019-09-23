# Hashmap / Dict

This article contains some typical problems that can be solve by hashmap. It is a useful data structure when we want to store previous states of some key.

## [Leetcode 560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
> Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

**Solution:** Keep track of the current sum `total`, if their exist some value `total - k` 
```python
def subarraySum(self, nums: List[int], k: int) -> int:
    count = {0:1}
    res, total = 0, 0
    for n in nums:
        total += n
        res += count.get(total - k, 0)
        count[total] = count.get(total, 0) + 1
    return res
```

## [Leetcode 316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)
> Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

**Solution:** Using a hashmap to keep track of the frequency of each character. Iterate through the given string, if we find current char is smaller than previous char and the previous char will occur in later substring, then we can safely delete the previous char. What's left in our result string will be the lexicographical smallest substring.

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, int> count, visited;
        for (auto c : s) count[c]++;
        
        string res = "";
        for (auto c : s) {
            count[c]--;
            if (visited[c]) continue;
            while (!res.empty() && c < res.back() && count[res.back()] > 0) {
                visited[res.back()] = 0;
                res.pop_back();
            }
            res += c;
            visited[c] = 1;
        }
        return res;
    }
};
```


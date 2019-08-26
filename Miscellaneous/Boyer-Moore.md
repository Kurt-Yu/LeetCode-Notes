# Boyer-Moore Majority Vote Algorithm

This article describes the details of Boyer-Moore algorithm and its application. It is usually used to find the majority element in some sequence within one pass (linear time) and constant space. For your reference, please see [this site](http://www.cs.utexas.edu/~moore/best-ideas/mjrty/).

The basic idea is this: 
+ We iterate through the sequence while maintain two things: candidate `e` and a `counter`.
+ If the counter is 0, we set the current candidate to e and we set the counter to 1.
+ If the counter is not 0, we increment or decrement the counter according to whether e is the current candidate.

We can think about it in this way: Image there are groups of people playing a game. We randomly pick two player from group (could be in the same group). If they are from the same group, we put them back and do nothing. If thet're not, then we kick them out of the game. In the end, all the player left are from the same group. (兑子战术，如果两个棋子类型不同，则相互抵消，剩下的一定是占比多的那个类型).

## [Leetcode 169. Majority Element](https://leetcode.com/problems/majority-element/)
> Given an array of size n, find the majority element. The majority element is the element that appears more than `⌊ n/2 ⌋` times.

```python
def majorityElement(self, nums: List[int]) -> int:
    res, count = None, 0
    for n in nums:
        if count == 0:
            res = n
            count = 1
        else:
            if res == n: count += 1
            else: count -= 1
    return res
```


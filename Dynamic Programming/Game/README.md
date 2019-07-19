# Game related DP Problems

This ariticle includes some game related problems, which typically need us to find the maximum score for some player. Below are some similar problems and my attempted solutions.

## [Leetcode 877. Stone Game](https://leetcode.com/problems/stone-game/)
> Given an array of stones, each stone has a score associated with it. Total length is even, and total score is odd so there will be no tie, A and B are two players want to play this game. One person can only take one stone each turn, either from the begining or the end of the array. Whoever get more score win the game. If A starts first, determine if he/she can win this game.

**Solution:** 
+ A takes first one or the last one.
+ Then B takes whatever. What B takes doesn't really matter. It is important that B wants A get minimum score after B takes one stone.
+ Recursive relation: `max(piles[i] + min(helper(i + 2, j), helper(i + 1, j - 1)), piles[j] + min(helper(i, j - 2), helper(i + 1, j - 1)))`
+ `helper()` is a function where two parameters are starting and ending index of `piles` array.
+ There are a lot of duplicated computation going on, so we use `memo` to store the cache.

```python
def stoneGame(self, piles: List[int]) -> bool:
    memo = {}
    
    def helper(i, j):
        if i > j: return 0
        if i == j and i < len(piles): return piles[i]
        if (i, j) in memo: return memo[(i, j)]
        
        res = max(piles[i] + min(helper(i + 2, j), helper(i + 1, j - 1)), \
                    piles[j] + min(helper(i, j - 2), helper(i + 1, j - 1)))
        memo[(i, j)] = res
        return res
    
    Alex = helper(0, len(piles) - 1)
    Lee = sum(piles) - Alex
    return Alex - Lee > 0
```

**Solution 2:**
+ Notice that the first person can always take even index element, or odd index element.
+ Since the total score is odd. There is no tie.
+ Whoever starts the first can win this game.

```python
def stoneGame(self, piles: List[int]) -> bool:
    return True
```

"""
Leetcode 191: https://leetcode.com/problems/number-of-1-bits/
"""

def hammingWeight(self, n):
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res
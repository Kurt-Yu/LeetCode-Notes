"""
Leetcode 435: https://leetcode.com/problems/non-overlapping-intervals/
"""
def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
    res = 0
    end = float('-inf')
    for i in sorted(intervals, key = lambda l : l.end):
        if i.start >= end:
            end = i.end
        else:
            res += 1
    return res
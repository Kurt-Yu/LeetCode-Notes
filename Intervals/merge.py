"""
Leetcode 56: https://leetcode.com/problems/merge-intervals/
"""
def merge(self, intervals: List[Interval]) -> List[Interval]:
    stack = []
    for i in sorted(intervals, key = lambda l : l.start):
        if stack and i.start <= stack[-1].end:
            stack[-1].end = max(i.end, stack[-1].end)
        else:
            stack.append(i)
    return stack
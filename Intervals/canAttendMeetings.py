"""
Leetcode 252: https://leetcode.com/problems/meeting-rooms/
"""
def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    intervals.sort(key=lambda i : i.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i-1].end: return False
    return True
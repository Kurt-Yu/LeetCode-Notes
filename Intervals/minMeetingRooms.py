"""
Leetcode 253: https://leetcode.com/problems/meeting-rooms-ii/
"""
def minMeetingRooms(self, intervals: List[Interval]) -> int:
    heap = []
    for i in sorted(intervals, key = lambda l : l.start):
        if heap and i.start >= heap[0]:
            heapq.heapreplace(heap, i.end)
        else:
            heapq.heappush(heap, i.end)
    return len(heap)
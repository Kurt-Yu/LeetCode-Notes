# Interval Problems

+ [Leetcode 56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
+ [Leetcode 252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
+ [Leetcode 253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
+ [Leetcode 435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

This artical is a summary of interval related algorithmic problems. This kind of problems can often be solved by `tree-like` data structures (like `priority queue`). I will first provide a general template and we will go through a few examples.

## Template

Step 1 would be sort the list of intervals based on the starting time (or ending time, depends on the senario). Python provides two sort functions: `list.sort()` and `sorted(list)`. The first is a in-place sort, the second returns a new sorted list. I personally would perfer the first one: 
```python
# set a `key` to the sort function
intervals.sort(key = lambda i : i.start)
# Or:
for i in sorted(intervals, key = lambda l : l.start):
    ...
```

Step 2 would be go through the sorted list, do whatever the problem asks to do (mergin the overlapping range, or arrange extra rooms).

## [Leetcode 56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
> Given a collection of intervals, merge all overlapping intervals.

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []
    for i in intervals:
        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], i[1])
        else:
            res.append(i)
    return res
```

## [Leetcode 252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
> Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine if a person could attend all meetings.

Solution: the same as the last problem.
```python
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
```

## [Leetcode 253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
> Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find the minimum number of conference rooms required.

**Solution:** use a heap to store the `end` time for each interval, if an interval's starting time is greater than the smallest ending time in heap (denoted by `heap[0]`, since the first item in a heap would always be the smallest one), that means this room can be used. Otherwise, we allocate a new room.

```python
    def minMeetingRooms(self, intervals):
        import heapq
        
        intervals.sort()
        heap = []
        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])

        return len(heap)
```

## [Leetcode 435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
> Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Solution: if there exists an averlap bewteen two intervals, keep the one which has the smaller ending time.

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key = lambda i : i[0])
    res = 0
    temp = []
    for i in intervals:
        if temp and i[0] < temp[-1][1]:
            res += 1
            if i[1] < temp[-1][1]:
                temp[-1] = i
        else:
            temp.append(i)
    return res
```
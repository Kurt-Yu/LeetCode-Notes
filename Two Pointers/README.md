# Two Pointers
Two Pointers is a typical algorithms design technique. It is used when we want to manipulate or do some operation on a already sorted list (or doubly linked list), which can dramatically decrease the running time. 

Here is a typical problem that can be solved using two pointers: Given an array of integers `A` sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

If we simply calculate the square of each number, then sort the list, that would be `O(nlogn)` time complexity. By comparing the left and right element of list, we can reduce the time complexity to `O(n)`

## Two Pointers in Linked List

### [Leetcode 142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
> Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`. 
 
```python
def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next: return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head
```

### [Leetcode234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
> Given a singly linked list, determine if it is a palindrome.

> Could you do it in O(n) time and O(1) space?
```python
def isPalindrome(self, head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    temp = self.reverse(slow)
    while temp and head:
        if temp.val != head.val: return False
        temp = temp.next
        head = head.next
    return True

def reverse(self, node):
    prev, curr = None, node
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev
```

## Two Pointers in Array
### [Leetcode 977](https://leetcode.com/problems/squares-of-a-sorted-array/)
```python
def sortedSquares(self, A: List[int]) -> List[int]:
    res = []
    left, right = 0, len(A) - 1
    while left <= right:
        l, r = abs(A[left]), abs(A[right])
        if l < r:
            res.insert(0, r * r)
            right -= 1
        else:
            res.insert(0, l * l)
            left += 1
    return res
```

### [Leetcode 941. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)
> Given an array A of integers, return true if and only if it is a valid mountain array. Recall that A is a mountain array if and only if:

```
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
```

**Idea**: use two pointers `i & j`, starting from the begining and the end, update each pointer if the next one is strictly larger than current. The terminate condition would be `0 < i == j < len(A) - 1`

```python
def validMountainArray(self, A: List[int]) -> bool:
    i, j = 0, len(A) - 1
    while i + 1 < len(A) and A[i + 1] > A[i]:
        i += 1
    while j - 1 >= 0 and A[j - 1] > A[j]:
        j -= 1
    return 0 < i == j < len(A) - 1
```

### [Leetcode 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
> Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

This solution came from [this post](https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.). The basic idea was to use two pointers, starts from the begining and the end, keep track of `leftmax` and `rightmax`. Base on which one is greater, we update the corresponding pointer. And we store `current_max - current_actual_value` (like a bucket).

```python
def trap(self, height: List[int]) -> int:
    i, j = 0, len(height) - 1
    res = 0
    leftmax = rightmax = 0
    while i <= j:
        leftmax = max(leftmax, height[i])
        rightmax = max(rightmax, height[j])
        if leftmax < rightmax:
            res += leftmax - height[i]
            i += 1
        else:
            res += rightmax - height[j]
            j -= 1
    return res
```

### [Leetcode 15. 3Sum](https://leetcode.com/problems/3sum/)
> Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

> The solution set must not contain duplicate triplets.

Idea: Sort the array first, for each element in the array, apply two sum algorithm to the rest of the array. Unlike the real 2Sum problem in leetcode (where we used hashmap to store the index and actual value), we just need to keep track of two pointers from the begining and the end (since this array is already sorted). The duplicate elements are handled by `if i > 0 and nums[i] == nums[i - 1]: continue`. And if we found a pair that satisfy the condition, we also need to remove the duplicates using `while j < k and nums[j] == nums[j + 1]` statement.

Time Complexity: `O(n^2)`

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                total -= nums[j]
                j += 1
            elif total > 0:
                total -= nums[k]
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j, k = j + 1, k - 1
    return res
```
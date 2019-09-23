# Linked List

This article includes some typical linked list leetcode problems.

*Reverse:*
+ [Leetcode 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
+ [Leetcode 234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

*Merge:*
+ [Leetcode 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
+ 

## Reverse Linked Lists
### [Leetcode 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Iterative solution:
```python
def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev
```

Recursive solution:
```python
def reverseList(self, head: ListNode) -> ListNode:
    def helper(node, prev = None):
        if not node: return prev
        next = node.next
        node.next = prev
        return helper(next, node)
    return helper(head)
```

### [Leetcode 234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

> Given a singly linked list, determine if it is a palindrome. Could you do it in O(n) time and O(1) space?

The idea is to use two pointers, `slow & fast` to find the middle node, then reverse the second half, compare the reversed half with the first half.

```python 
def isPalindrome(self, head: ListNode) -> bool:
    if not head: return True
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    # reverse the second half
    prev, curr = None, slow
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    
    # compare the first half and reversed second half
    while prev and head:
        if prev.val != head.val: return False
        prev, head = prev.next, head.next
    return True
```

## Merge Linked Lists

### [Leetcode 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

This problem is the base senario of all merging-based list problems. The idea is that given two (or more) sorted linked list, return a new list that is also sorted.

```python
# Method 1: Iterative solution
def mergeTwoLists(self, l1, l2):
    res = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return res.next

# Method 2: Recursive solution
def mergeTwoLists(self, l1, l2):
    if not l1 or not l2: 
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
```

### [Leetcode 23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
Since we already know how to merge two sorted lists, for `k` sorted lists, one natrual way is to use **divide and conqure**. Divide `k` lists into two parts, and repeat this process over and over again, until we reach a base case where we only have one list left, then use the `merge two lists` routine.

```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists: return None
    if len(lists) == 1: return lists[0]
    i = len(lists) // 2
    l1 = self.mergeKLists(lists[:i])
    l2 = self.mergeKLists(lists[i:])
    return self.merge(l1, l2)
    
def merge(self, l1, l2):
    res = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return res.next
```

Another version, using `heap (Priority Queue)`:
```python
import heapq

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    res = curr = ListNode(0)
    h = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(h)

    while h:
        val, i, node = h[0]
        if not node.next:
            heapq.heappop(h)
        else:
            heapq.heapreplace(h, (node.next.val, i, node.next))
        curr.next = node
        curr = curr.next
    return res.next
```

One thing that worth note here is that in `Python 3`, the comparision operator `<, >` does not support equal values in terms of priorities. If we were only to store `(node.val, node)` to the heap, that means when there is a tie, the internal comparision operator will try to compare the actual `node`. But a `node` object is not comparable. That's why we added a index   `i` in the heap, when there is a tie, we then use `i` to compare.

## Sort Linked List

### [Leetcode 148. Sort List](https://leetcode.com/problems/sort-list/)
> Sort a linked list in O(n log n) time using constant space complexity.

Solution: Apply merge sort to original list. This is a combination of merge and two pointers.
```python
def sortList(self, head: ListNode) -> ListNode:
    if not head or not head.next: return head
    curr, slow, fast = None, head, head
    while fast and fast.next:
        curr = slow
        slow = slow.next
        fast = fast.next.next
    curr.next = None
    
    left,right = self.sortList(head), self.sortList(slow)
    res = self.merge(left, right)
    return res

def merge(self, left, right):
    curr = res= ListNode(0)
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    curr.next = left or right
    
    return res.next
```

## Remove Node

### [Leetcode 19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
> Given a linked list, remove the n-th node from the end of list and return its head.

Solution: use two pointers to find the total number of nodes in this list. Then remove the node based on relation between `n` and `count`. This is a one pass solution.

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    count = 0
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        count += 1
    
    total = count * 2 if not fast else count * 2 + 1
    if n == total: return head.next
    n = total - n
    
    if n > count:
        for _ in range(n - count - 1):
            slow = slow.next
        slow.next = slow.next.next
    else:
        curr = head
        for _ in range(n - 1):
            curr = curr.next
        curr.next = curr.next.next
    return head
```

## Loop / Cycle (Two Pointers)

This section contains some typical problems that can be solved by two poiters (slow & fast). It is a useful technique when you want to deal with cycles and loops in a linked list.

### [Leetcode 160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
> Write a program to find the node at which the intersection of two singly linked lists begins.

```python
def getIntersectionNode(self, headA, headB):
    if not headA or not headB: return None

    # If pointer points to the end of a linked list, just switch to the other list
    # Terminate condition: either two pointers points to None, or they are the same
    pa, pb = headA, headB
    while pa is not pb:
        pa = headB if not pa else pa.next
        pb = headA if not pb else pb.next

    return pa
```

### [Leetcode 287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
> Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

```python
def findDuplicate(self, nums):
    if not nums: return 0
    
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow =  nums[slow]
        fast = nums[nums[fast]]
    
    fast = 0
    while fast != slow:
        fast, slow = nums[fast], nums[slow]
    return fast
```

### [Leetcode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
> Given a linked list, determine if it has a cycle in it.

```python    
def hasCycle(self, head):
    if not head: return False
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: return True
    return Falsepython
```

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
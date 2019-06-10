# Linked List

This article includes some typical linked list leetcode problems.

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







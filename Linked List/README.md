# Linked List

This article includes some typical linked list leetcode problems.

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




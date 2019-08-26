# LRU cache

LRU stands for `least recently used`. The idea is that, in real world software applications, they tend to store some recently used computation result in a cache. Those computations might be expensive or time consuming such as I/O operation or database fetch, we don't need to do those operations over and over again beacuse we can get the result directly from cache when the same input is given. But such cache has a fixed size. When we reaches the capacity, it is a natural to remove those `least recently used` cache. That's how this problem comes. We need to design such data structure that can support `get` and `put` operation in constant time.

Using a dictionary (or hashmap) is not enough. Since we have to keep track of the time those result were added. A traditional hashmap has no particular order, so how can we maintain the order (by time) while remove unnecessary result in constant time? The answer is to use a `doubly linked list`. Whenever we `get` a node, we remove it from its original position in the list, then add it to the tail of list. Whenever we `put` a new node, we add it the tail of list, then check if the capacity reaches, if so, remove the least recently used cache (in this case, the head node). 

Here are the full implementation of this data structure:
## [Leetcode 146. LRU Cache](https://leetcode.com/problems/lru-cache/)

```Python
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
```

Most programming languages have some advanced data strucutres build-in. Python has `OrderedDict`, which is in `collections` module. By using `OrderedDict`, we can achieve the exactly same thing as we did above. But this approach is not recommended in an interview.

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = collections.OrderedDict()
    
    def get(self, key):
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1
    
    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
            
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)
```
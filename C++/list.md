# List

Lists are sequence containters that allow non-contiguous memory allocation. It has slow traversal, but once a position has been found, insertion and deletion are quick. C++ List are doubly linked list.

**Functions:**
```cpp
// Access Elements:
front() - returns the first element in the list
back() - returns the last element in the list

// Modify Elements:
push_front(g), push_back(g) - add element at front or end of list
pop_front(), pop_back() - removes the first ot last element of list
insert(), erase() - insert or erase element at a given position
reverse() - reverses the list
sort() - sort the list in increasing order

// Iterator:
begin(), end() - returns a begin or end iterator
rbegin(), rend() - reversed version of above functions
cbegin(), cend() - constant version of above functions
crbeing(), crend() - reversed & constant version of above functions
```
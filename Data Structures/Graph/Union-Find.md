# Union Find

Union Find (or disjoint set) is such a data structure that keeps track of elements partitioned into a number of disjoint (non-overlapping) subsets. There are usually two operations associated with this data strucutre: `union` and `find`. As the name suggests, `union` unions two distinct sets, where `find` finds which set a particular element belongs. 

Suppose we have three vertices, `0`, `1` and `2`. We can keep track of an array of length `3`. Initially, all elements are set to be the same as vertice label (e.g `array = [0, 1, 2]`), meaning that each vertice is in its own connected component, because initially there is no edge. Node `0` is in a connected component named `0` and node `1` is in a connected component named `1`.... As we adding edges to this graph, we then gradually manipulate this array, to union connected component together. For example:
```python
# Initially the array is
 0  1  2
[0, 1, 2]

# For edge 0-1, first find the subsets where node `0` and `1` are. 
# Then choose any one of the set to be the parent of the other.
# In this case, we make node `1` as the parent of node `0`
 0  1  2
[1, 1, 2]

# For edge 1-2, similar as before, we make node `2` the parent of node `1`
 0  1  2
[1, 2, 2]
```

This data structure is useful to detect cycle in undirected graph (but only works with graphs that has no self-loops). To tell whether there is a cycle, we can iterate through all edges, for each edge, if the two vertices belongs to the same set, then there must be a cycle.

Two basic operations: `union` & `find`:
```Python
def find(parent, i):
    if parent[i] == i: return i
    return find(parent, parent[i])

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    parent[xroot] = yroot
```

The above code is correct but could be time-consuming in some cases. Image this case: the parent of node `1` is node `2`, the parent of node `2` is node `3`, the parent of node `3` is node `4`. To find the which set node `1` was in, we have to traversal all the way to node `4`. This is essentially a linear time search. To improve that, we can have a rank assocaited with each node. The rank of this node means how many subtree it has. Whenever we union two sets, we first compare the rank of `root1` and `root2`, then make the node with smaller rank to be the child of the larger one. In this way, the tree we build is more balance, thus decreasing the searching time. This technique is known as `union by rank and path compression`.

```python
def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)
    if rank[rootx] < rank[rooty]:
        preant[rootx] = rooty
    elif rank[rootx] > rank[rooty]:
        parent[rooty] = rootx
    else:
        parent[rooty] = rootx
        rank[rootx] += 1
```

## [Leetcode 547. Friend Circles](https://leetcode.com/problems/friend-circles/)
> There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

> Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

**Solution:** The `find` and `union` operation is almost the same as we described above, except we maintain a variable `count`. Decreasing `count` whenever we do a `union` operation. 

```python
def findCircleNum(self, M: List[List[int]]) -> int:
    def find(parent, i):
        if parent[i] == i: return i
        return find(parent, parent[i])
    
    def union(parent, rank, x, y, count):
        x, y = find(parent, x), find(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
        count -= 1
        return count
    
    parent = list(range(len(M)))
    rank = [0] * len(M)
    count = len(M)
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            if M[i][j] == 1 and find(parent, i) != find(parent, j):
                count = union(parent, rank, i, j, count)
            
    return count
```
# Vector

Vectors are `dynamicly resize array`. Vector elements are stored in contiguous storage so that they can be accessed and traversed using iterators. Insert & Remove element at the end takes `O(1)` time. Insert & erasing at the middle or front takes `O(n)` time.

**Initialization:**
```cpp
// Method 1: init by pushing element one by one:
vec.push_back(1);
vec.push_back(2);
vec.push_back(3);

// Method 2: specify size and default value:
vector<int> vec(5, 10);     // size 5 of all values as 10

// Method 3: init like normal array:
vector<int> vec{10, 20, 30};

// Method 4: init from array
int arr[] = {10, 20, 30};
int size = sizeof(arr) / sizeof(arr[0]);
vector<int> vec(arr, arr + size);

// Method 5: init from another vector:
vector<int> vec1 {10, 20, 30};
vector<int> vec2(vec1.begin(), vec1.end());
```

**Iterators:**
```cpp
begin() - returns an iterator pointing to the first element in the vector
end() - returns an iterator pointing to the last element in the vector
rbegin() - reversed version of `begin()`
rend() - reversed version of `end()`
cbegin(), cend(), crbegin(), crend() are constant version (hardly used)
```
Example:
```cpp
for (auto it = vec.begin(); it != vec.end(); it++) cout << *it << " ";
// Output of begin and end: 1 2 3 4 5

for (auto it = vec.rbegin(); it != vec.rend(); it++) cout << *it << " ";
// Output of rbegin and rend: 5 4 3 2 1
```

**Capacity:**
```cpp
size() - returns the size of elements in the vector
empty() - returns weather the container is empty
resize(n) - resize the container so that it contains `n` elements
max_size(), capacity(), shrink_to_fit(), reserve() are hardly used
```

**Element Access:**
```cpp
[] - access element using index, just like array
at(i) - returns a reference to the element at position `i`
front() - returns a reference to the first element in the vector
back() - returns a reference to the last element in the vector
```
Example:
```cpp
for (int i = 1; i <= 10; i++) vec.push_back(i);
cout << vec[2] << endl;         // print 3
cout << vec.at(4) << endl;      // print 5
cout << vec.front() << endl;    // print 1
cout << vec.back() << endl;     // print 10
```

**Modifiers:**
```cpp
assign() - assigns new value to the vector elements by replacing old ones
push_back() - push element to the back
pop_back() - pop element from the back
insert() - inserts element at a given position
erase() - remove element at a given position
swap() - swap contents of one vector with another vector with same type
clear() - remove all elements
emplace(), emplace_back() are same as insert()
```
Example:
```cpp
vec.assign(5, 10);              // fill the vector with 10 five times
vec.push_back(15);  cout << vec[vec.size() - 1] << endl;    // 15
vec.pop_back();                 // now vector is 10, 10, 10, 10, 10
vec.insert(vec.begin(), 5); cout << vec[0] << endl;     // 5
vec.erase(vec.begin()); cout << vec[0] << endl;         // 10
vec.emplace(vec.begin(), 5); cout << vec[0] << endl;    // 5
vec.emplace_back(20); cout << vec[vec.size() - 1] << endl;  // 20

v1: [1, 2]
v2: [3, 4]
v1.swap(v2);    // now v1: [3, 4], v2: [1, 2]
```

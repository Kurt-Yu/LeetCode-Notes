#include <iostream>
#include <unordered_map>
#include <list>
#include <utility>

using namespace std;

int main() {
    unordered_map<int, list<pair<int, int>>::iterator> map;
    list<pair<int, int>> list;

    pair<int, int> test = make_pair(1, 2);
    list.push_back(test);
    map[1] = list.begin();

    auto it = map.find(1);

    cout << it->second->second << endl;
    return 0;
}
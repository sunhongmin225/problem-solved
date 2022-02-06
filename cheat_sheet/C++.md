# C++ Cheat Sheet

## Assumptions
* Necessary headers are already included
* `using namespace std;` is declared at the beginning

## C++ STL

### Map

#### Check if `key` exists in map

```
map<string, int> my_map;
string key = "this_is_key";
if (my_map.find(key) != my_map.end()) {
    // key exists in my_map
} else {
    // key does not exist in my_map
}
```

#### Get char at index from string

```
string my_str = "abcd";
char my_char = my_str.at(1); // my_char == b
```

#### Insert an item into map

```
map<string, int> my_map;
my_map["football"] = 11;
```

### Queue

#### Insert an item into queue

```
queue<int> my_queue;
my_queue.push(11);
```

### Set

#### Insert an item into set

```
set<int> my_set;
my_set.insert(11);
```

### Stack

#### Insert an item into stack

```
stack<int> my_stack;
my_stack.push(11);
```

### Vector

#### Insert an item into vector

```
vector<int> my_vector;
my_vector.push_back(11);
```

## Conversion

### String to Integer
```
string age_str = "27";
int age_int = stoi(age_str);
```

## Handling Inputs

### Example 1

```
/*
Input:
2 3 4
*/

int a, b, c;
scanf("%d %d %d", &a, &b, &c);
```

### Example 2

```
/*
Input:
2
GCF
ACDEB
*/

#define MAX 10

int n;
scanf("%d\n", &n);
vector<string> strs;
for (int i = 0; i < n; i++) {
    char tmp[MAX];
    scanf("%s", tmp);
    string str = tmp;
    strs.push_back(str);
}
```

## Math-related

### Power

```
#include <cmath>
int my_int = pow(2, 5); // my_int == 2^5 == 32
```

## Struct

### Declaration

```
struct Person {
    unsigned int age;
    unsigned int height;
    unsigned int weight;
    string name;
};
```

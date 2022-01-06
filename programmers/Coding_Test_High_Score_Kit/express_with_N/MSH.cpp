/*
1. Handle edge cases necessarily (e.g., when number == N, when number == concat).
2. Pass address of collections (i.e., vector<set<int>>& record, set<int>& s).
3. Return right away if possible.
4. Get used to cpp collections grammar (e.g., s.find(number) != s.end()).
*/
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <iostream>

#define MAX_USE 8

using namespace std;

int calculate (vector<set<int>>& record, set<int>& s1, set<int>& s2, int idx, int number) {

    set<int> s = record[idx];
    for (auto i1 : s1) {
        for (auto i2 : s2) {
            // return right away if target number is calculated
            if (i1 + i2 == number || i1 * i2 == number || i1 - i2 == number || i1 / i2 == number)
                return idx;
            // add to set only when calculation result > 0
            if (i1 + i2 > 0) s.insert(i1 + i2);
            if (i1 - i2 > 0) s.insert(i1 - i2);
            if (i1 * i2 > 0) s.insert(i1 * i2);
            if (i1 / i2 > 0) s.insert(i1 / i2);
        }
    }
    record[idx] = s;
    return -1;
}

int solution (int N, int number) {
    // handle minor edge cases
    if (number == N)
        return 1;
    vector<set<int>> record;

    // dummy empty_set to ignore 0th index
    set<int> empty_set;
    record.push_back(empty_set);

    // handle concatenation
    for (int i = 1; i <= MAX_USE; i++) {
        set<int> s;
        int concat = 0;
        for (int j = 0; j < i; j++) {
            concat += pow(10, j) * N;
        }
        s.insert(concat);
        record.push_back(s);
    }

    for (int i = 2; i <= MAX_USE + 1; i++) {
        // return -1 if you use more than MAX_USE Ns
        if (i == MAX_USE + 1)
            return -1;

        set<int> s = record[i];
        // handle edge cases where number == concat
        if (s.find(number) != s.end())
            return i;

        // divide-and-conquer
        for (int j = i - 1; j >= i / 2; j--) {
            int first = j;
            int second = i - j;
            set<int> s1 = record[first];
            set<int> s2 = record[second];
            int idx = calculate(record, s1, s2, i, number);
            if (idx != -1)
                return idx;
        }
    }

    return -1;
}
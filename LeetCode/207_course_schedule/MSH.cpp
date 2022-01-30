/*
1. First time coding topological sort
2. Aid from: https://www.geeksforgeeks.org/detect-cycle-in-directed-graph-using-topological-sort/
3. Need to practice using DFS, topological sort, stack, ...
*/
#include <vector>
#include <unordered_map>
#include <stack>

using namespace std;

class Solution {
public:
    void topological_sort (int id, unordered_map<int, pair<bool, vector<int>>> &courses, stack<int> &s) {
        courses[id].first = true;
        for (int i = 0; i < courses[id].second.size(); i++) {
            if (!courses[courses[id].second[i]].first) {
                topological_sort(courses[id].second[i], courses, s);
            }
        }
        s.push(id); // add to stack if no dependency exists
    }

    bool cycle_exists (stack<int> &s, vector<vector<int>>& prereq) {
        // stores the position of nodes in topological order
        unordered_map<int, int> pos;
        int idx = 0;

        // pop all elements from stack
        while (!s.empty()) {
            pos[s.top()] = idx;
            s.pop();
            idx++;
        }

        for (int i = 0; i < prereq.size(); i++) {
            // if topological order is interrupted, then cycle exists
            if (pos[prereq[i][0]] > pos[prereq[i][1]]) { return true; }
        }

        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        unordered_map<int, pair<bool, vector<int>>> courses; // key: course id, val: pair of 'visited' and neighbor nodes (course ids)
        for (int i = 0; i < prerequisites.size(); i++) {
            if (prerequisites[i][0] == prerequisites[i][1]) { return false; } // handle edge case
            courses[prerequisites[i][0]].first = false; // 'visited' is false by default
            courses[prerequisites[i][0]].second.push_back(prerequisites[i][1]); // push_back neighbor nodes
        }

        stack<int> s; // stacks course ids in topological order
        unordered_map<int, pair<bool, vector<int>>>::iterator it;
        for (it = courses.begin(); it != courses.end(); it++) {
            if (!(it->second).first) { // topological_sort only for unvisited nodes
                topological_sort(it->first, courses, s);
            }
        }

        if (cycle_exists(s, prerequisites)) { return false; } // cannot meet prerequisite conditions

        return true;
    }
};

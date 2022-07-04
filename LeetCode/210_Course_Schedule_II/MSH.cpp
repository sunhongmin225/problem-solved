#include <vector>
#include <queue>

using namespace std;

class Solution {
struct Node {
    int id;
    int num_incoming_edges;
    int num_outgoing_edges;
    bool visited;
    vector<Node *> nexts;
};
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> answer;

        // handle edge case
        if (prerequisites.size() == 0) {
            for (int i = 0; i < numCourses; i++) { answer.push_back(i); }
            return answer;
        }

        vector<Node> nodes; // vector holding all courses in form of Node
        queue<int> start_node_ids; // queue holding nodes with num_incoming_edges of 0

        for (int i = 0; i < numCourses; i++) {
            nodes.push_back(Node());
            nodes[i].id = i;
            nodes[i].num_incoming_edges = 0;
            nodes[i].num_outgoing_edges = 0;
            nodes[i].visited = false;
        }

        for (int i = 0; i < prerequisites.size(); i++) {
            int src_id = prerequisites[i][1];
            int trgt_id = prerequisites[i][0];
            nodes[src_id].num_outgoing_edges++;
            nodes[trgt_id].num_incoming_edges++;
            nodes[src_id].nexts.push_back(&nodes[trgt_id]);
        }

        // push nodes whose num_incoming_edges == 0 to start_node_ids queue
        for (int i = 0; i < numCourses; i++) {
            if (nodes[i].num_incoming_edges == 0) { start_node_ids.push(i); }
        }

        while (!start_node_ids.empty()) {
            int start_id = start_node_ids.front();
            start_node_ids.pop();
            answer.push_back(start_id);
            for (int i = 0; i < nodes[start_id].nexts.size(); i++) {
                nodes[start_id].nexts[i]->num_incoming_edges--;
                if (nodes[start_id].nexts[i]->num_incoming_edges == 0) { start_node_ids.push(nodes[start_id].nexts[i]->id); }
            }
        }

        if (answer.size() != numCourses) { answer.clear(); }
        return answer;
    }
};

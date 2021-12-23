#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

struct Node {
    int id;
    int cost;
    bool visited;
    vector<int> neigh;
};

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;

    vector<Node> nodes;
    nodes.reserve(n);

    nodes.push_back(Node());
    nodes[0].id = 0;
    nodes[0].cost = 0;
    nodes[0].visited = true;

    for (int i = 1; i < n; i++) {
        nodes.push_back(Node());
        nodes[i].id = i;
        nodes[i].cost = 0;
        nodes[i].visited = false;
    }

    for (int i = 0; i < edge.size(); i++) {
        int first = edge[i][0] - 1;
        int second = edge[i][1] - 1;
        nodes[first].neigh.push_back(second);
        nodes[second].neigh.push_back(first);
    }

    queue<Node> nodes_queue;
    nodes_queue.push(nodes[0]);

    while (!nodes_queue.empty()) {
        Node curr = nodes_queue.front();
        nodes_queue.pop();
        for (int i = 0; i < curr.neigh.size(); i++) {
            if (!nodes[curr.neigh[i]].visited) {
                nodes[curr.neigh[i]].visited = true;
                nodes[curr.neigh[i]].cost = curr.cost + 1;
                nodes_queue.push(nodes[curr.neigh[i]]);
            }
        }
    }

    int max_distance = -1;
    for (int i = 0; i < n; i++) {
        if (nodes[i].cost > max_distance) {
            max_distance = nodes[i].cost;
        }
    }

    for (int i = 0; i < n; i++) {
        if (nodes[i].cost == max_distance) {
            answer++;
        }
    }

    return answer;
}
/*
1. Frequent approach: solving BFS using queue -> should be used to it
2. Cheat sheet will be very helpful e.g., q.front(); q.pop();
3. Access with address (&) to actually make changes to instances
*/
#include <iostream>
#include <vector>
#include <queue>

#define MAX_N 100
#define MAX_M 100

using namespace std;

struct Box {
	int x;
	int y;
	char status;
	bool visited;
	int cost;
};

int main () {

	int N, M;
	scanf("%d %d\n", &N, &M);
	vector<vector<Box>> maze;
	queue<Box> q;
	for (int i = 0; i < N; i++) {
		vector<Box> row;
		for (int j = 0; j < M; j++) {
			char status;
			if ( (i == N - 1 && j == M - 1) || (j != M - 1) ) { scanf("%c", &status); }
			else { scanf("%c\n", &status); }
			row.push_back(Box());
			row[j].x = i;
			row[j].y = j;
			row[j].status = status;
			if (i == 0 && j == 0) { row[j].visited = true; row[j].cost = 1; q.push(row[j]); }
			else { row[j].visited = false; row[j].cost = MAX_N * MAX_M + 1; }
		}
		maze.push_back(row);
	}

	int answer = 0;
	while (!q.empty()) {
		Box curr_box = q.front();
		q.pop();
		if (curr_box.x == N - 1 && curr_box.y == M - 1) {
			answer = curr_box.cost;
			break;
		}

		if (curr_box.x != 0) {
			Box *up_box = &maze[curr_box.x - 1][curr_box.y];
			if (up_box->status == '1' && !up_box->visited) {
				up_box->visited = true;
				up_box->cost = curr_box.cost + 1;
				q.push(*up_box);
			}
		}
		if (curr_box.x != N - 1) {
			Box *down_box = &maze[curr_box.x + 1][curr_box.y];
			if (down_box->status == '1' && !down_box->visited) {
				down_box->visited = true;
				down_box->cost = curr_box.cost + 1;
				q.push(*down_box);
			}
		}
		if (curr_box.y != 0) {
			Box *left_box = &maze[curr_box.x][curr_box.y - 1];
			if (left_box->status == '1' && !left_box->visited) {
				left_box->visited = true;
				left_box->cost = curr_box.cost + 1;
				q.push(*left_box);
			}
		}
		if (curr_box.y != M - 1) {
			Box *right_box = &maze[curr_box.x][curr_box.y + 1];
			if (right_box->status == '1' && !right_box->visited) {
				right_box->visited = true;
				right_box->cost = curr_box.cost + 1;
				q.push(*right_box);
			}
		}
	}

	printf("%d\n", answer);
	return 0;
}

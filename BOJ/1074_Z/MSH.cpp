/*
1. 'Z' is kind of a deception to make you think this problem is complicated :/
2. Divide-and-conquer
3. Finding recurrence relation is important
*/
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int base_case (int r, int c) {
	if (r == 0 && c == 0) { return 0; }
	else if (r == 0 && c == 1) { return 1; }
	else if (r == 1 && c == 0) { return 2; }
	else if (r == 1 && c == 1) { return 3; }
	return -1; // should not reach here
}

vector<int> to_lower_dim (int r, int c, int order) {
	int offset = pow(2, order);
	vector<int> answer;
	if (r - offset >= 0 && c - offset >= 0) {
		answer.push_back(r - offset);
		answer.push_back(c - offset);
		answer.push_back(3);
		return answer;
	} else if (r - offset >= 0 && c >= 0) {
		answer.push_back(r - offset);
		answer.push_back(c);
		answer.push_back(2);
		return answer;
	} else if (r >= 0 && c - offset >= 0) {
		answer.push_back(r);
		answer.push_back(c - offset);
		answer.push_back(1);
		return answer;
	} else if (r >= 0 && c >= 0) {
		answer.push_back(r);
		answer.push_back(c);
		answer.push_back(0);
		return answer;
	}
	return answer; // should not reach here
}

int main () {
	// hanlde inputs
	int N, r, c;
	scanf("%d %d %d", &N, &r, &c);

	int answer = 0;

	// handle base case
	if (N == 1) {
		answer = base_case(r, c);
		printf("%d\n", answer);
		return 0;
	}

	int curr_r = r;
	int curr_c = c;
	// iterate until base case (2*2 matrix) is met
	for (int i = N - 1; i >= 1; i--) {
		vector<int> intermediate_result = to_lower_dim(curr_r, curr_c, i);
		curr_r = intermediate_result[0];
		curr_c = intermediate_result[1];
		int quadrant = intermediate_result[2];
		answer += quadrant *  pow(pow(2, i), 2);
	}

	answer += base_case(curr_r, curr_c);

	printf("%d\n", answer);
	return 0;
}

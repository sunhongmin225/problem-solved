#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}

int solution(vector<pair<int, int>>& meetings, int N) {
    int answer = 0;

    sort(meetings.begin(), meetings.end(), comp);

    int curr_end = 0;
    for (int i = 0; i < N; i++) {
        if (meetings[i].first >= curr_end) {
            curr_end = meetings[i].second;
            answer++;
        }
    }

    return answer;
}

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> meetings;
    meetings.reserve(N);

    for (int i = 0; i < N; i++) {
        int start;
        int end;
        cin >> start >> end;
        meetings.push_back(make_pair(start, end));
    }

    cout << solution(meetings, N) << endl;

    return 0;
}
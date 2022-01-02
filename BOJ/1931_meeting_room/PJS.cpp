#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool compare(pair <int,int> p1, pair <int,int> p2) { // compare 함수
    if (p1.second == p2.second) { 
        return p1.first < p2.first; // start time
    }
    return p1.second < p2.second; // end time
}


int get_max_meetings(vector<pair<int, int>>  meetings) {
  sort(meetings.begin(), meetings.end(), compare);

  int prev_end_time = 0;
  int max_meetings = 0;

  for (int i = 0 ; i < meetings.size() ; i++) {
    pair<int, int> meeting = meetings[i];
    //assert(meeting.first < meeting.second);  // assertion fails on BOJ

    if (prev_end_time <= meeting.first) {
      max_meetings += 1;
      prev_end_time = meeting.second;
    }
  } 

  return max_meetings;
}

int main() {
  int N;
  cin >> N;

  vector<pair<int, int>> meetings;
  string start, end;
  
  for (int i = 0 ; i < N ; i++) { 
    cin >> start >> end;
    meetings.push_back(pair<int, int>(stoi(start), stoi(end)));
  }

  int max_meetings = get_max_meetings(meetings);
  cout << max_meetings << endl;
}


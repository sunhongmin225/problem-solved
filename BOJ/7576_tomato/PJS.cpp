#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// for some reason, split and count were not found (maybe some link error...)
// so I needed to implemenet them myself.... ㅠㅠ
vector<int> split(string input, char delimiter) {
    // splits the input string according to the delimiter
    vector<int> answer;
    stringstream ss(input);
    string temp;
    while (getline(ss, temp, delimiter)) {
        answer.push_back(stoi(temp));
    }
    return answer;
}


int count(vector<int> vec, int element) {
    // counts the number of 'elements' in vec
    int cnt = 0;
    for(auto elem : vec) {
        if (elem == element) {cnt++;}
    }
    return cnt;
}


int main() {
    int M, N;
    string line; 
    getline(cin, line);

    M = split(line, ' ')[0];
    N = split(line, ' ')[1];

    // box keeps the tomatoes, and just_changed is a queue that holds the index positions
    // in the box (e.g. (3, 2)) for the tomatoes that have become ripe.
    vector<vector<int>> box;
    queue<pair<int, int>> just_changed;

    int num_lines = 0;
    while(num_lines < N) {
        string line; 
        getline(cin, line);
        box.push_back(split(line, ' '));
        num_lines++;
        if (num_lines == N) {break;}
    }

    // 1. check if given tomatoes are all ripe already
    bool all_ripe = true;
    for (int i = 0 ; i < N ; i++) {
        if(count(box[i], 0)) {
            all_ripe = false;
            break;
        }
    }

    if (all_ripe) {return 0;}   // if all ripe in the first place, return 0

    // 2. calculate the number of days for all tomatoes to get ripe

    // 2-1. put all the ripe tomatoes in the queue
    for (int i = 0 ; i < N ; i ++) {
        for (int j = 0 ; j < M ; j++) {
            if (box[i][j] == 1) {
                just_changed.push(make_pair(i, j));
            }
        }
    }

    // 2-2. add (-1,-1) as a indicator between days
    just_changed.push(make_pair(-1,-1));    // indicator for next day

    int days = -1;
    
    // 2-3. updates the ripe tomatoes until there no newly riped tomatoes are added
    while(!just_changed.empty()) {
        pair<int, int> location = just_changed.front();
        just_changed.pop();
        int i = location.first;
        int j = location.second;

        if (i == -1 && j == -1) {
            days++; 
            if (!just_changed.empty()) {just_changed.push(make_pair(-1,-1));}
            continue;
        }

        if (i-1 >= 0 && box[i-1][j] == 0) {box[i-1][j] = 1; just_changed.push(make_pair(i-1, j));}
        if (i+1 < N && box[i+1][j] == 0) {box[i+1][j] = 1; just_changed.push(make_pair(i+1, j));}
        if (j-1 >= 0 && box[i][j-1] == 0) {box[i][j-1] = 1; just_changed.push(make_pair(i, j-1));}
        if (j+1 < M && box[i][j+1] == 0) {box[i][j+1] = 1; just_changed.push(make_pair(i, j+1));}
    }

    // 3. if there are any 0's (non-ripe tomatoes) in the box, then it means they cannot be reached
    for (int i = 0 ; i < N ; i++) {
        if(count(box[i], 0)) {return -1;}
    }

    return days;
}

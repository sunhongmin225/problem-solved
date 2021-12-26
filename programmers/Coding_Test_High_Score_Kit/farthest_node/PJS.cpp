#include <climits>
#include <tuple>
#include <queue>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
  int connectivity[n][n];
    
  for (int i = 0 ; i < n ; i++) {
    for (int j = 0 ; j < n ; j++) {
      connectivity[i][j] = 0;
      }
  }
    
  int distance[n];
  distance[0] = 0;
  for (int i = 1 ; i < n ; i++) {
    distance[i] = INT_MAX;
  }
    
  for (auto e : edge) {
    int p1 = e[0]-1;
    int p2 = e[1]-1;
    connectivity[p1][p2] = 1;
    connectivity[p2][p1] = 1;
  }
    
  queue<tuple<int, int, int>> q;
    
  for (int i = 0 ; i < n ; i++) {
    if (connectivity[0][i]) {
      q.push(make_tuple(0,i,1));
    }
  }
    
  while (!q.empty()) {
    tuple<int, int, int> e = q.front();
    q.pop();
    int start_node = get<0>(e);
    int end_node = get<1>(e);
    int dist = get<2>(e);
    
    int min_dist = distance[end_node];
    
    if (dist < min_dist) {
      distance[end_node] = dist;
  
      for (int i = 0 ; i < n ; i++) {
        if (connectivity[end_node][i]) {
          if(dist + 1 < distance[i]) {
            tuple<int, int, int> t(end_node, i, dist+1);
            q.push(t);
          }
        }
      }
    }   
  }
    
  int max_dist = 0;
  int answer = 0;
  for (int i = 0 ; i < n ; i++) {
    if (distance[i] > max_dist) {
      max_dist = distance[i];
      answer = 1;
    } else if (distance[i] == max_dist) {
      answer++;
    }
  }
  
  return answer;
}

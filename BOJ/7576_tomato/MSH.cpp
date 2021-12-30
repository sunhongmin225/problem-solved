/*
1. scanf is (way) faster than cin!
2. No need to set visited flag since there are other conditions (e.g., status).
3. BFS is (way) better than a simple recursion.
*/
#include <vector>
#include <queue>
#include <iostream>
#include <cstdio>

using namespace std;

struct Tomato {
    int x;
    int y;
    int status;
    int days;
};

int main () {

    // handle inputs
    int M, N;
    scanf("%d %d\n", &M, &N);
    vector<vector<Tomato>> storage;
    queue<Tomato> queue_tomatoes;
    for (int i = 0; i < N; i++) {
        vector<Tomato> tomatoes;
        for (int j = 0; j < M; j++) {
            int status;
            scanf("%d", &status);
            tomatoes.push_back(Tomato());
            tomatoes[j].x = i;
            tomatoes[j].y = j;
            tomatoes[j].status = status;
            tomatoes[j].days = 0;
            // only add to queue when status is 1
            if (status == 1)
                queue_tomatoes.push(tomatoes[j]);
        }
        storage.push_back(tomatoes);
    }

    // perform BFS
    while (!queue_tomatoes.empty()) {
        Tomato tomato = queue_tomatoes.front();
        queue_tomatoes.pop();
        // boundary check is necessary for all directions
        if (tomato.x - 1 >= 0 && storage[tomato.x - 1][tomato.y].status == 0) {
            storage[tomato.x - 1][tomato.y].status = 1;
            storage[tomato.x - 1][tomato.y].days = tomato.days + 1;
            queue_tomatoes.push(storage[tomato.x - 1][tomato.y]);
        }
        if (tomato.x + 1 < N && storage[tomato.x + 1][tomato.y].status == 0) {
            storage[tomato.x + 1][tomato.y].status = 1;
            storage[tomato.x + 1][tomato.y].days = tomato.days + 1;
            queue_tomatoes.push(storage[tomato.x + 1][tomato.y]);
        }
        if (tomato.y - 1 >= 0 && storage[tomato.x][tomato.y - 1].status == 0) {
            storage[tomato.x][tomato.y - 1].status = 1;
            storage[tomato.x][tomato.y - 1].days = tomato.days + 1;
            queue_tomatoes.push(storage[tomato.x][tomato.y - 1]);
        }
        if (tomato.y + 1 < M && storage[tomato.x][tomato.y + 1].status == 0) {
            storage[tomato.x][tomato.y + 1].status = 1;
            storage[tomato.x][tomato.y + 1].days = tomato.days + 1;
            queue_tomatoes.push(storage[tomato.x][tomato.y + 1]);
        }
    }

    // find max_days for each tomato
    int max_days = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            // check if there are unripe tomatoes
            if (storage[i][j].status == 0) {
                printf("%d\n", -1);
                return 0;
            }
            if (storage[i][j].days > max_days) {
                max_days = storage[i][j].days;
            }
        }
    }
    printf("%d\n", max_days);

    return 0;
}

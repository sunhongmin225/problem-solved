#include <iostream>
#define MAX_N 46
using namespace std;

int main(){
    int N;
    long long fib[MAX_N];
    cin >> N;

    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= N; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    cout << fib[N] << endl;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K, num = 1;
    cin >> N >> K;
    for(int i = 0; i < N; i++) {
        if(num * 2 >= num + K) {
            num += K;
        } else {
            num *= 2;
        }
    }
    cout << num << endl;
}
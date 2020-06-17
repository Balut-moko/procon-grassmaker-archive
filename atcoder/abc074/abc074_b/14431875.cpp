#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K, ans = 0;
    cin >> N >> K;
    for(int i = 0; i < N; i++) {
        int x;
        cin >> x;
        if(x <= K - x) {
            ans += x * 2;
        } else {
            ans += (K - x) * 2;
        }
    }

    cout << ans << endl;
}
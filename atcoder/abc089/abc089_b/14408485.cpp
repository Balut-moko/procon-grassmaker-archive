#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string ans;
    cin >> N;
    for(int i = 0; i < N; i++) {
        string S;
        cin >> S;
        if(S == "Y") {
            ans = "Four";
            break;
        }
    }
    if(ans=="Four"){
        cout << ans << endl;
    }else{
        ans = "Three";
        cout << ans << endl;
    }}
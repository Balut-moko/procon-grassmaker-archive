#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, num, sum = 0;
    cin >> N;
    num = N;
    while(num) {
        int num_temp;
        num_temp = num % 10;
        sum += num_temp;
        num = num / 10;
    }
    if(N % sum == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
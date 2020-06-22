#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,Asum=0,Avg;
  cin >> N;
  vector<int> vec(N);
  
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }
  for (int i = 0; i < N; i++) {
    Asum += vec.at(i);
  }
  Avg = Asum / N;
  for (int i = 0; i < N; i++) {
    if (Avg >= vec.at(i)){
      cout << Avg - vec.at(i) << endl;
    } else {
      cout << vec.at(i) - Avg << endl;
    }
  }
}

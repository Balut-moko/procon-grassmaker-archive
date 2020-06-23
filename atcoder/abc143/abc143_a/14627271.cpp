#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, ans;
  cin >> A >> B;
  if(A <= B * 2){
    ans=0;
  }else{
    ans = A - B * 2;
  }
  cout << ans << endl;
}

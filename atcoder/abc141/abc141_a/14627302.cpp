#include <bits/stdc++.h>
using namespace std;

int main() {
  string S,ans;
  cin >> S;
  ans = "Sunny";
  if(S == "Sunny"){
    ans = "Cloudy";
  }else if(S == "Cloudy"){
    ans = "Rainy";
  }
  cout << ans << endl;
}

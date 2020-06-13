#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int s,s_temp,ans;
  cin >> s;
  ans=0;

  ans = ans + s/100;
  s_temp = s-s/100*100;
  ans = ans + s_temp/10;
  s_temp = s_temp-s_temp/10*10;
  ans = ans + s_temp;
    
  cout << ans << endl;
}
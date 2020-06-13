#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N,N_temp,a,b,c,d;
  cin >> N;
  a=N/1000;
  N_temp=N%1000;
  b=N_temp/100;
  N_temp=N_temp%100;
  c=N_temp/10;
  d=N_temp%10;
  
  if (a==b && a==c) {
    cout << "Yes" << endl;
  }
  else if (b==c && c==d){
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }
}

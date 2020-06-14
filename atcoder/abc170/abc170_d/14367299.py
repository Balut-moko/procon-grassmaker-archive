#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Amax=A[-1]+1
    dp = [True]*Amax
    ans=0
    a_temp=set()
    a_tempcheck=set()
    for a in A:
        if dp[a]:
            ans+=1
            a_temp.add(a)
            for i in range(a, Amax, a):
                dp[i] = False
        else:
            if a not in a_tempcheck:
                if a in a_temp:
                    ans-=1
                    a_tempcheck.add(a)
    print(ans)
    
if __name__ == "__main__":
    main()

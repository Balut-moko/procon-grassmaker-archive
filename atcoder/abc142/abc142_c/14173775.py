#!/usr/bin/env python3

def main():
    N=int(input())
    A = list(map(int,input().split()))
    ans=[None]*N
    i=1
    for a in A:
        ans[a-1]=str(i)
        i+=1
    print(' '.join(ans))

if __name__ == "__main__":
    main()

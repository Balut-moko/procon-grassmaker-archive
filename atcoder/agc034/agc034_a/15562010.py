#!/usr/bin/env python3

def main():
    N, A, B, C, D = map(int, input().split())
    S = input()
    ans = 'Yes'
    if C <D:
        if '##' in S[B-1:D] or '##' in S[A-1:C]:
            ans = 'No'
    else:
        if '##' in S[A-1:C] or '...' not in S[B-2:D+1]:
            ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    n = int(input())
    S = []
    P = []
    for i in range(n):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    print('atcoder' if sum(P) / 2 - max(P) >= 0 else S[P.index(max(P))])


if __name__ == "__main__":
    main()

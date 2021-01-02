#!/usr/bin/env python3

def main():
    n = int(input())
    S = [input() for _ in range(n)]
    S0 = set()
    S1 = set()
    for s in S:
        if '!' in s:
            S1.add(s[1:])
        else:
            S0.add(s)
    S01 = S0 & S1
    print(S01.pop() if S01 else 'satisfiable')


if __name__ == "__main__":
    main()

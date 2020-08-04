#!/usr/bin/env python3
import itertools


def main():
    N = int(input())
    S = [input() for i in range(N)]
    S_cnt = [0]*5
    E = ["M", "A", "R", "C", "H"]
    for s in S:
        for i in range(5):
            if s[0] ==E[i]:
                S_cnt[i] += 1
    E_list = list(itertools.combinations(E, 3))
    tmp = 1
    ans = 0
    for e in E_list:
        for i in range(3):
            for j in range(5):
                if e[i] == E[j]:
                    tmp *= S_cnt[j]
        ans += tmp
        tmp = 1
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import itertools


def main():
    n, k = map(int, input().split())
    TravelTimes = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for v in itertools.permutations(range(1, n)):
        tmp = 0
        before = 0
        for i in v:
            tmp += TravelTimes[before][i]
            before = i
        tmp += TravelTimes[before][0]
        if tmp == k:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()

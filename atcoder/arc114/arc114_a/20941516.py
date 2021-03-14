#!/usr/bin/env python3
import math


def main():
    n = int(input())
    X = sorted(map(int, input().split()))
    prime_num = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    ans = 10**30
    for i in range(1, 2**15):
        tmp = 1
        for j in range(15):
            if ((i >> j) & 1):
                tmp *= prime_num[j]

        for x in X:
            if math.gcd(x, tmp) == 1:
                break
        else:
            ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()

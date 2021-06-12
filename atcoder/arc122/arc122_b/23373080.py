#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)

    def solve(x):
        tmp = x * n + sum_a
        for i in range(n):
            tmp -= min(a[i], 2 * x)
        return tmp / n
    low = 0
    high = 10**18
    while low + pow(10, -6) < high:
        c1 = (low * 2 + high) / 3
        c2 = (low + high * 2) / 3
        if solve(c1) > solve(c2):
            low = c1
        else:
            high = c2
    print(solve(low))


if __name__ == "__main__":
    main()

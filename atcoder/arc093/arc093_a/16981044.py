#!/usr/bin/env python3

def main():
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    dist = [abs(a[i] - a[i - 1]) for i in range(1, n + 2)]
    total = sum(dist)
    ans = [0] * n
    for i in range(n):
        ans[i] = total - dist[i] - dist[i + 1] + abs(a[i] - a[i + 2])
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()

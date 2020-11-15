#!/usr/bin/env python3


def main():
    n, w = map(int, input().split())
    Water = [list(map(int, input().split())) for _ in range(n)]
    a = [0] * (2 * 10**5 + 1)
    for water in Water:
        a[water[0]] += water[2]
        a[water[1]] -= water[2]
    cumsum = [0] * (2 * 10**5 + 2)
    for i in range(1, len(a)):
        cumsum[i] = cumsum[i - 1] + a[i - 1]
    print('Yes' if max(cumsum) <= w else 'No')


if __name__ == "__main__":
    main()

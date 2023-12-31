#!/usr/bin/env python3


def main():
    n, m = map(int, input().split())
    x = sorted(map(int, input().split()))
    x_dist = sorted([x[i] - x[i - 1] for i in range(1, m)], reverse=True)
    print(x[-1] - x[0] - sum(x_dist[:n - 1]))


if __name__ == "__main__":
    main()

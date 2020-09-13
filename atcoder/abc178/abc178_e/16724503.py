#!/usr/bin/env python3

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for i in range(n)]
    max_z, max_w, min_z, min_w = -10**20, -10**20, 10**20, 10**20
    ans = 0
    for p in xy:
        max_z, max_w = max(max_z, p[0] + p[1]), max(max_w, p[0] - p[1])
        min_z, min_w = min(min_z, p[0] + p[1]), min(min_w, p[0] - p[1])
    ans = max(max_z - min_z, max_w - min_w)
    print(ans)


if __name__ == "__main__":
    main()

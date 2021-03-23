#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    xy = [[False] * n for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        xy[x - 1][y - 1] = xy[y - 1][x - 1] = True
    ans = 1
    for bit in range(2**n):
        flg = True
        for i in range(n):
            for j in range(i):
                if bit >> i & bit >> j & 1 and not xy[i][j]:
                    flg = False
        if flg:
            ans = max(ans, bin(bit).count("1"))

    print(ans)


if __name__ == "__main__":
    main()

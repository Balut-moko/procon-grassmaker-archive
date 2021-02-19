#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(m - 1):
        for j in range(i + 1, m):
            tmp = 0
            for k in range(n):
                tmp += max(a[k][i], a[k][j])
            ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()

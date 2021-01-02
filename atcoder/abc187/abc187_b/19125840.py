#!/usr/bin/env python3

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            if abs((xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0])) <= 1:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    n = int(input())
    xy = [list(map(int, input().split()))for _ in range(n)]
    ans = 'No'
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (xy[k][0] - xy[i][0]) * (xy[j][1] - xy[i][1]) == (xy[j][0] - xy[i][0]) * (xy[k][1] - xy[i][1]):
                    ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()

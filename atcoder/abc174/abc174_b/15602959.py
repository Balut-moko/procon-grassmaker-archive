#!/usr/bin/env python3

def main():
    N, D = map(int, input().split())
    xy = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        d = xy[i][0]**2 + xy[i][1]**2
        if D**2 >= d:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()

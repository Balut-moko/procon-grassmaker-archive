#!/usr/bin/env python3

def main():
    n, time = map(int, input().split())
    ans = 1001
    for i in range(n):
        c, t = map(int, input().split())
        if t <= time:
            ans = min(ans, c)
    print(ans if ans != 1001 else 'TLE')


if __name__ == "__main__":
    main()

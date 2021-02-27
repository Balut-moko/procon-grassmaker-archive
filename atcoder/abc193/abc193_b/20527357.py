#!/usr/bin/env python3

def main():
    n = int(input())
    ans = 10**10
    for i in range(n):
        a, p, x = map(int, input().split())
        x -= a
        if 0 < x:
            ans = min(ans, p)

    print(ans if ans != 10**10 else -1)


if __name__ == "__main__":
    main()

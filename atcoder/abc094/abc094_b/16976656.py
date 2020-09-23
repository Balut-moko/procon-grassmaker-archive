#!/usr/bin/env python3

def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(m):
        if a[i] > x:
            ans = min(i, len(a) - i)
            break
    else:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    arg = round(sum(a) / len(a))
    ans = 0
    for i in range(N):
        ans += (a[i] - arg)**2
    print(ans)


if __name__ == "__main__":
    main()

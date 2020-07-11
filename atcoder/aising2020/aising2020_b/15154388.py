#!/usr/bin/env python3

def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if i % 2 == 0 and (a[i] % 2 == 1):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

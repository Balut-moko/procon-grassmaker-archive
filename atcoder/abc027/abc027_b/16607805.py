#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    if sum(a) % n != 0:
        ans = -1
    else:
        avg = sum(a) // n
        tmp = 0
        for i in range(n - 1):
            if a[i] != avg:
                tmp = a[i] - avg
                a[i] = avg
                a[i + 1] += tmp
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()

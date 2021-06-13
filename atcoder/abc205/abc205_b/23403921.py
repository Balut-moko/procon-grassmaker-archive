#!/usr/bin/env python3

def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    ans = 'Yes'
    for i in range(1, n + 1):
        if i != a[i - 1]:
            ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()

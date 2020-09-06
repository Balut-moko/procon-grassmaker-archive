#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    arr = sorted([list(map(int, input().split())) for i in range(n)])
    for ab in arr:
        k -= ab[1]
        if k <= 0:
            ans = ab[0]
            break

    print(ans)


if __name__ == "__main__":
    main()

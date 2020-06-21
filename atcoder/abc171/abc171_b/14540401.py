#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    p.sort()
    ans = 0
    for k in range(K):
        ans += p[k]
    print(ans)


if __name__ == "__main__":
    main()

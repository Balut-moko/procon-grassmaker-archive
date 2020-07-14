#!/usr/bin/env python3

def main():
    N = int(input())
    a = list(map(int, input().split()))

    INF = 1 << 60
    a_sum = [0] * (N + 1)
    for i in range(N):
        a_sum[i + 1] = a_sum[i] + a[i]
    ans = INF
    for i in range(1,N):
        ans = min(ans, abs(a_sum[i] - (a_sum[N] - a_sum[i])))
    print(ans)


if __name__ == "__main__":
    main()

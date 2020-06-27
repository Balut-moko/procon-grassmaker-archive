def main():
    N = int(input())
    h = list(map(int, input().split()))
    INF = 10**30
    h_dp = [INF] * N
    h_dp[0] = 0
    for i in range(1, N):
        h_dp[i] = min(h_dp[i], h_dp[i - 1] + abs(h[i] - h[i - 1]))
        if i > 1:
            h_dp[i] = min(h_dp[i], h_dp[i - 2] + abs(h[i] - h[i - 2]))
    print(h_dp[N - 1])


if __name__ == "__main__":
    main()

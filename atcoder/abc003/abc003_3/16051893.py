def main():
    N, K = map(int, input().split())
    R = sorted(map(int, input().split()))
    ans = 0
    for i in range(N - K, N):
        ans = (ans + R[i]) / 2
    print(ans)


if __name__ == "__main__":
    main()

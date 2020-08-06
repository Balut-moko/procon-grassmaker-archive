def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        tmp = 1 / N
        cnt = i
        while cnt < K:
            tmp /= 2
            cnt *= 2
        ans += tmp
    print(ans)


if __name__ == "__main__":
    main()

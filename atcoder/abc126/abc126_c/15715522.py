def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1 / N
        else:
            tmp = i
            cnt = 0
            while True:
                tmp *= 2
                cnt += 1
                if tmp >= K:
                    break
            ans += 1 / N * (1 / 2)**cnt
    print(ans)


if __name__ == "__main__":
    main()

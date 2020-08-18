def main():
    N, Q = map(int, input().split())
    S = input()
    lr = [list(map(int, input().split())) for i in range(Q)]
    Cumsum = [0] * (N + 1)
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            Cumsum[i + 1] = Cumsum[i] + 1
        else:
            Cumsum[i + 1] = Cumsum[i]

    for q in range(Q):
        ans = Cumsum[lr[q][1]] - Cumsum[lr[q][0]]
        print(ans)


if __name__ == "__main__":
    main()

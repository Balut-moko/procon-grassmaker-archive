def main():
    N, M = map(int, input().split())
    ab = [None] * N
    for i in range(N):
        ab[i] = list(map(int, input().split()))

    cd = [None] * M
    for j in range(M):
        cd[j] = list(map(int, input().split()))
    ans = [None] * N
    for i in range(N):
        Md = 10**16
        for j in range(M):
            Md_temp = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
            if Md > Md_temp:
                Md = Md_temp
                ans[i] = j + 1

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()

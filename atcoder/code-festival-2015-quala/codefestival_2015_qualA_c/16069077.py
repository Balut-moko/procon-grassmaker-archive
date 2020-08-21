def main():
    N, T = map(int, input().split())
    Asum, Bsum = 0, 0
    ABlist = []
    for i in range(N):
        AB = list(map(int, input().split()))
        AB.append(AB[0] - AB[1])
        ABlist.append(AB)
        Asum += AB[0]
        Bsum += AB[1]
    ABlist.sort(key=lambda x: x[2], reverse=True)
    if Bsum > T:
        ans = -1
    else:
        ans = 0
        while Asum > T:
            Asum -= ABlist[ans][2]
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()

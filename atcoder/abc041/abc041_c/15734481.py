def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = []
    for i in range(N):
        AA.append([A[i], i + 1])
    AA.sort(reverse=True)
    for i in range(N):
        print(AA[i][1])


if __name__ == "__main__":
    main()

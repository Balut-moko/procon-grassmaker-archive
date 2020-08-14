def main():
    N = int(input())
    A = sorted(map(int, input().split()), reverse=True)
    print(A[0] + sum(A[1:(N - 2) // 2 + 1]) * 2 + A[(N - 2) // 2 + 1] * (N % 2))


if __name__ == "__main__":
    main()

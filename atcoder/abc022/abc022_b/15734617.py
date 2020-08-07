def main():
    N = int(input())
    A = {int(input()) for i in range(N)}
    ans = N - len(A)
    print(ans)


if __name__ == "__main__":
    main()

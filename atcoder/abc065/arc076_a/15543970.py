import math


def main():
    N, M = map(int, input().split())
    mod = 10 ** 9 + 7
    if abs(N - M) > 1:
        ans = 0
    elif N - M == 1:
        ans = (math.factorial(M)**2 * N) % mod
    elif N - M == -1:
        ans = (math.factorial(N)**2 * M) % mod
    else:
        ans = (math.factorial(N)**2 * 2) % mod

    print(ans)


if __name__ == "__main__":
    main()

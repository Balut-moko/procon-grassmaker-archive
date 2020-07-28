import math


def main():
    N = int(input())
    ans = math.factorial(N)
    mod = 10**9 + 7
    print(ans % mod)


if __name__ == "__main__":
    main()

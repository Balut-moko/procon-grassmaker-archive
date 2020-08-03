import collections


def main():
    n = int(input())
    ans = 10**10
    for i in range(10 ** 5):
        for j in range(10 ** 5):
            if i * j > n:
                break
            else:
                ans = min(ans, abs(i - j) + n - i * j)
    print(ans)


if __name__ == "__main__":
    main()

import math


def main():
    n = int(input())
    ans = n
    for i in range(n + 1):
        cnt = 0
        t = i
        while t > 0:
            cnt += t % 6
            t //= 6
        j = n - i
        while j > 0:
            cnt += j % 9
            j //= 9
        ans = min(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()

import collections


def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    cnt = collections.Counter(A)
    ans = 0
    for v in cnt.values():
        ans += v - 1
    print(ans)


if __name__ == "__main__":
    main()

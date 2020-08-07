import collections


def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    cnt = collections.Counter(A)
    ans = len(A) - len(cnt)
    print(ans)


if __name__ == "__main__":
    main()

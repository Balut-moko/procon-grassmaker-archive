import collections


def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = collections.Counter(A)
    ans = 0
    for k, v in counter.items():
        if v > k:
            ans += v - k
        elif v < k:
            ans += v
    print(ans)


if __name__ == "__main__":
    main()
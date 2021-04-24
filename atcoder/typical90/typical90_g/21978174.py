import bisect


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    q = int(input())
    b = [int(input()) for _ in range(q)]
    for i in range(q):
        idx = bisect.bisect_left(a, b[i])
        if idx == 0:
            print(abs(a[idx] - b[i]))
        elif idx == n:
            print(abs(a[-1] - b[i]))
        else:
            print(min(abs(a[idx] - b[i]), abs(a[idx - 1] - b[i])))


if __name__ == "__main__":
    main()

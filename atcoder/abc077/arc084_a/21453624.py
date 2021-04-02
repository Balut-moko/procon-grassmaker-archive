import bisect


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    c = sorted(map(int, input().split()))
    ans = 0
    for i in range(n):
        a_tmp = bisect.bisect_left(a, b[i])
        c_tmp = n - bisect.bisect_right(c, b[i])
        ans += a_tmp * c_tmp
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    re_a = list(zip(*a))
    ans = [[0] * w for _ in range(h)]
    sum_a = [sum(a[i]) for i in range(h)]
    sum_re_a = [sum(re_a[i]) for i in range(w)]
    for i in range(h):
        for j in range(w):
            ans[i][j] = sum_a[i] + sum_re_a[j] - a[i][j]
    for tmp in ans:
        print(*tmp)


if __name__ == "__main__":
    main()

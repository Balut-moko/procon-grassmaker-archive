#!/usr/bin/env python3

def main():
    n, m, t = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    flag = True
    tmp = n - ab[0][0]
    if tmp <= 0:
        flag = False
    for i in range(m - 1):
        tmp = min(n, tmp + ab[i][1] - ab[i][0])
        tmp -= ab[i + 1][0] - ab[i][1]
        if tmp <= 0:
            flag = False
    tmp = min(n, tmp + ab[-1][1] - ab[-1][0])
    tmp -= t - ab[-1][1]
    if tmp <= 0:
        flag = False
    print('Yes' if flag else 'No')


if __name__ == "__main__":
    main()

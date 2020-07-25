#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    money = 1000
    for i in range(N - 1):
        if cnt > 0:
            money += cnt * A[i]
            cnt = 0
        if A[i] < A[i + 1]:
            cnt, money = divmod(money, A[i])
    if cnt > 0:
        money += cnt * A[N - 1]
        cnt = 0
    print(money)


if __name__ == "__main__":
    main()

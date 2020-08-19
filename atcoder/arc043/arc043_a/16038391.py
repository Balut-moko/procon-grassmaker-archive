#!/usr/bin/env python3

def main():
    N, A, B = map(int, input().split())
    S = [int(input()) for i in range(N)]

    flag = False
    B_tmp = max(S) - min(S)
    if B_tmp > 0:
        P = B / B_tmp
        flag = True

    if flag:
        Q = A - P * sum(S) / N
        print(P, Q)
    else:
        print(-1)


if __name__ == "__main__":
    main()

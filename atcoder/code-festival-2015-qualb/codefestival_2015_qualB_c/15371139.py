#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)
    B_cnt = 0
    flag = True
    if N < M:
        flag = False
    else:
        for i in range(N):
            if A[i] >= B[B_cnt]:
                B_cnt += 1
                if B_cnt == M:
                    break
            else:
                flag = False
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()

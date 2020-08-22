#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    tmp_max = 0
    ans = 0
    for i in range(N):
        if A[i] < tmp_max:
            ans += tmp_max - A[i]
        else:
            tmp_max = A[i]
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    N = int(input())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        temp = sum(A1[0:i + 1]) + sum(A2[i:N])
        ans = max(ans, temp)

    print(ans)


if __name__ == "__main__":
    main()

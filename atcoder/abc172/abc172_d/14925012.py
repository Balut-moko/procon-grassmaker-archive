#!/usr/bin/env python3

def main():
    N = int(input())

    def fanc(N):
        return N * (N + 1) // 2
    ans = 0
    for i in range(1, N + 1):
        ans += i * fanc(N // i)
    print(ans)


if __name__ == "__main__":
    main()

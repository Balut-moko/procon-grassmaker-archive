#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    s = input()
    c = [[n] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            if ord(s[i]) - ord('a') == j:
                c[i][j] = i
            else:
                c[i][j] = c[i + 1][j]
    ans = []
    now = 0
    for i in range(k):
        for j in range(26):
            pos = c[now][j]
            if k <= n - pos + i:
                ans.append(chr(ord('a') + j))
                now = pos + 1
                break

    print(*ans, sep='')


if __name__ == "__main__":
    main()

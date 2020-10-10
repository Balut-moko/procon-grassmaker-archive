#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    s = [input() for i in range(H)]
    ans = 0
    for h in range(H):
        for w in range(1, W):
            if s[h][w - 1] == s[h][w] == '.':
                ans += 1
    for h in range(H - 1):
        for w in range(W):
            if s[h][w] == s[h + 1][w] == '.':
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()

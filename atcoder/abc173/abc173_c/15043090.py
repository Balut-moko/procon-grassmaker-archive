#!/usr/bin/env python3

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            count = 0
            for n in range(H):
                for m in range(W):
                    if ((i >> n) & 1) == 0 and ((j >> m) & 1) == 0 and C[n][m] == '#':
                        count += 1

            if count == K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()

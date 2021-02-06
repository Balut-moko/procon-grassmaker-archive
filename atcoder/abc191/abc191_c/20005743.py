#!/usr/bin/env python3
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(1, H):
        for w in range(1, W):
            tmp = 0
            if S[h][w] == '#':
                tmp += 1
            if S[h - 1][w] == '#':
                tmp += 1
            if S[h][w - 1] == '#':
                tmp += 1
            if S[h - 1][w - 1] == '#':
                tmp += 1
            if tmp == 1 or tmp == 3:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()

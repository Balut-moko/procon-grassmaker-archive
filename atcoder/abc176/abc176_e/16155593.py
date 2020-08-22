#!/usr/bin/env python3

def main():
    H, W, M = map(int, input().split())
    bomb = [list(map(int, input().split()))for i in range(M)]
    H_bomb = [0] * (H + 1)
    W_bomb = [0] * (W + 1)
    for b in bomb:
        H_bomb[b[0]] += 1
        W_bomb[b[1]] += 1
    max_h, max_w = max(H_bomb), max(W_bomb)
    cnt = H_bomb.count(max_h) * W_bomb.count(max_w)
    for b in bomb:
        if H_bomb[b[0]] == max_h and W_bomb[b[1]] == max_w:
            cnt -= 1
    print(max_h + max_w + bool(cnt) - 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    W, H, N = map(int, input().split())
    xya = [list(map(int, input().split())) for i in range(N)]
    a, b = 0, 0
    for i in range(N):
        if xya[i][2] == 1:
            a = max(a, xya[i][0])
        elif xya[i][2] == 2:
            W = min(W, xya[i][0])
        elif xya[i][2] == 3:
            b = max(b, xya[i][1])
        elif xya[i][2] == 4:
            H = min(H, xya[i][1])
    print(max(0, W - a) * max(0, H - b))


if __name__ == "__main__":
    main()

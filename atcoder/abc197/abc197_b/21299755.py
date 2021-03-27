#!/usr/bin/env python3

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1
    ans = 1
    x_tmp = x
    while True:
        x_tmp -= 1
        if 0 <= x_tmp and s[x_tmp][y] == '.':
            ans += 1
        else:
            break
    x_tmp = x
    while True:
        x_tmp += 1
        if x_tmp < h and s[x_tmp][y] == '.':
            ans += 1
        else:
            break

    y_tmp = y
    while True:
        y_tmp -= 1
        if 0 <= y_tmp and s[x][y_tmp] == '.':
            ans += 1
        else:
            break
    y_tmp = y
    while True:
        y_tmp += 1
        if y_tmp < w and s[x][y_tmp] == '.':
            ans += 1
        else:
            break
    print(ans)


if __name__ == "__main__":
    main()

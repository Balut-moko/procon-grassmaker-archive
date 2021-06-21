#!/usr/bin/env python3

def main():
    h, w = map(int, input().split())
    if h == 1 or w == 1:
        ans = h * w
    else:
        h += 1
        w += 1
        ans = (h // 2) * (w // 2)
    print(ans)


if __name__ == "__main__":
    main()

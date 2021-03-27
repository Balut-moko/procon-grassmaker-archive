#!/usr/bin/env python3
import math


def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    px, py = (x0 + x1) / 2, (y0 + y1) / 2
    th = math.radians(360 / n)
    ans_x = ((x0 - px) * math.cos(th)) - ((y0 - py) * math.sin(th))
    ans_y = ((x0 - px) * math.sin(th)) + ((y0 - py) * math.cos(th))
    print(ans_x + px, ans_y + py)


if __name__ == "__main__":
    main()

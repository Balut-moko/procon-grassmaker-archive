#!/usr/bin/env python3

def main():
    x1, y1, r = map(int, input().split())
    x2, y2, x3, y3 = map(int, input().split())
    red = 'NO'
    blue = 'NO'
    point = [(x1 - r, y1), (x1, y1 - r), (x1 + r, y1 - r), (x1, y1 + r)]
    point2 = [(x2, y2), (x2, y3), (x3, y2), (x3, y3)]
    for p in point:
        if p[0] < x2 or p[0] > x3 or p[1] < y2 or p[1] > y3:
            red = 'YES'
    for p in point2:
        if r**2 < (x1 - p[0])**2 + (y1 - p[1])**2:
            blue = 'YES'

    print(red)
    print(blue)


if __name__ == "__main__":
    main()

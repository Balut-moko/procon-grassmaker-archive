#!/usr/bin/env python3

def main():
    r, x, y = map(int, input().split())
    dist = x**2 + y**2
    ans = 0
    while (r * ans) ** 2 < dist:
        ans += 1
    if ans == 1 and dist < r**2:
        ans = 2
    print(ans)


if __name__ == "__main__":
    main()

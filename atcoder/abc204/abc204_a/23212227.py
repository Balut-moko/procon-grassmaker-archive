#!/usr/bin/env python3

def main():
    x, y = map(int, input().split())
    if x == y:
        ans = x
    else:
        ans = 3 - x - y
    print(ans)


if __name__ == "__main__":
    main()

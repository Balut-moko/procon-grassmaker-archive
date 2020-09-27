#!/usr/bin/env python3

def main():
    ans = 0
    for i in range(3):
        s, e = map(int, input().split())
        ans += s * e // 10
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    a, b, c, d = map(int, input().split())
    ans = 'No'
    if abs(a - c) <= d or (abs(a - b) <= d and abs(b - c) <= d):
        ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()

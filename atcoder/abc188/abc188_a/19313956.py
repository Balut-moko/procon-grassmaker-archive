#!/usr/bin/env python3

def main():
    x, y = map(int, input().split())
    ans = 'No'
    if min(x, y) + 3 > max(x, y):
        ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()

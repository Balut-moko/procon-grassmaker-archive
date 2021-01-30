#!/usr/bin/env python3

def main():
    n, s, d = map(int, input().split())
    ans = 'No'
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            ans = 'Yes'

    print(ans)


if __name__ == "__main__":
    main()

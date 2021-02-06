#!/usr/bin/env python3

def main():
    v, t, s, d = map(int, input().split())
    ans = 'Yes'
    if v * t <= d <= v * s:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()

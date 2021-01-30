#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    if a > b - c:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'

    print(ans)


if __name__ == "__main__":
    main()

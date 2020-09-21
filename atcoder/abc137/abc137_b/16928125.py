#!/usr/bin/env python3

def main():
    k, x = map(int, input().split())
    ans = range(x - k + 1, x + k)
    print(*ans)


if __name__ == "__main__":
    main()

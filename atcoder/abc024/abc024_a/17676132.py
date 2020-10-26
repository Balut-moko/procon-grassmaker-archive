#!/usr/bin/env python3

def main():
    a, b, c, k = map(int, input().split())
    s, t = map(int, input().split())
    print(s * a + t * b - (s + t) * c * (k <= s + t))


if __name__ == "__main__":
    main()

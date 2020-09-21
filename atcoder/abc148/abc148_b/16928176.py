#!/usr/bin/env python3

def main():
    n = int(input())
    s, t = input().split()
    print(*[s[i] + t[i] for i in range(n)], sep="")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    n = int(input())
    S, T = input().split()
    print(*[s + t for s, t in zip(S, T)], sep="")


if __name__ == "__main__":
    main()

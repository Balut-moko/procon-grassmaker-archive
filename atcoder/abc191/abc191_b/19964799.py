#!/usr/bin/env python3

def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    li = [a for a in A if a != x]
    print(*li)


if __name__ == "__main__":
    main()

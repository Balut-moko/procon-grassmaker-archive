#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) <= min(b):
        print(len(list(range(max(a), min(b) + 1))))
    else:
        print(0)


if __name__ == "__main__":
    main()

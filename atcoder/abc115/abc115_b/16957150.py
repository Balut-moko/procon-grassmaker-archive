#!/usr/bin/env python3

def main():
    p = [int(input()) for i in range(int(input()))]
    print(sum(p) - max(p) // 2)


if __name__ == "__main__":
    main()

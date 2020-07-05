#!/usr/bin/env python3

def main():
    N = int(input())
    if N%1000 == 0:
        ans = 0
    else:
        ans = 1000 - N % 1000
    print(ans)


if __name__ == "__main__":
    main()

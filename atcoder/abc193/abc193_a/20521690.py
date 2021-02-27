#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    ans = 100*(a-b)/a

    print(ans)


if __name__ == "__main__":
    main()

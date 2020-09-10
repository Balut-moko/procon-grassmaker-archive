#!/usr/bin/env python3

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort(key=lambda x: x[::-1])
    print(*s, sep='\n')


if __name__ == "__main__":
    main()

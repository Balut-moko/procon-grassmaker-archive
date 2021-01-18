#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = 0
    c = 0
    for j in range(n):
        a_max = max(a_max, a[j])
        c = max(c, a_max * b[j])
        print(c)


if __name__ == "__main__":
    main()

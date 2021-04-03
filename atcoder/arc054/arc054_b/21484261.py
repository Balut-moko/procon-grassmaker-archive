#!/usr/bin/env python3

def main():
    p = float(input())

    def solve(x):
        return x + p * (2**(-x / 1.5))
    low = 0
    high = p
    cnt = 500
    while cnt > 0:
        cnt -= 1
        c1 = (low * 2 + high) / 3
        c2 = (low + high * 2) / 3
        if solve(c1) > solve(c2):
            low = c1
        else:
            high = c2

    print(solve(low))


if __name__ == "__main__":
    main()

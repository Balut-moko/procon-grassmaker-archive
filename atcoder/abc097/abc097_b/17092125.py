#!/usr/bin/env python3

def main():
    x = int(input())
    ans = 0
    for b in range(1, 1000):
        for p in range(2, 10):
            if x >= b ** p:
                ans = max(ans, b ** p)
    print(ans)


if __name__ == "__main__":
    main()

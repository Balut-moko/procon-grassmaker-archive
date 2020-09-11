#!/usr/bin/env python3

def main():
    n = int(input())
    ng = [int(input()) for i in range(3)]
    ans = "NO"
    for i in range(100):
        if n not in ng:
            if n - 3 not in ng:
                n -= 3
            elif n - 2 not in ng:
                n -= 2
            elif n - 1 not in ng:
                n -= 1
            else:
                break
    if n <= 0:
        ans = "YES"
    print(ans)


if __name__ == "__main__":
    main()

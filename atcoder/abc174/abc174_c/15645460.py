#!/usr/bin/env python3

def main():
    K = int(input())
    if K % 7 == 0:
        L = 9 * K / 7
    else:
        L = 9 * K
    if L % 2 == 0 or L % 5 == 0:
        ans = -1
    else:
        i = 1
        tmp = 10
        while True:
            tmp %= L
            if tmp == 1:
                ans = i
                break
            i += 1
            tmp *= 10

    print(ans)


if __name__ == "__main__":
    main()

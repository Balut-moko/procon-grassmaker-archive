#!/usr/bin/env python3

def main():
    n = int(input())
    if n == 1 or n == 2:
        print(0)
    elif n == 3:
        print(1)
    else:
        trib = [0] * 4
        trib[1] = 1
        for i in range(3, n):
            trib[0] = (trib[1] + trib[2] + trib[3]) % 10007
            trib[1], trib[2], trib[3] = trib[0], trib[1], trib[2]
        print(trib[0] % 10007)


if __name__ == "__main__":
    main()

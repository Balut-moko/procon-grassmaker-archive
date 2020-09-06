#!/usr/bin/env python3

def main():
    n = int(input())

    for i in range(10**4):
        if n <= i * (i + 1) / 2:
            tmp = i
            break
    tmpsum = tmp * (tmp + 1) / 2
    if n == tmpsum:
        for i in range(1, tmp + 1):
            print(i)
    else:
        for i in range(1, tmp + 1):
            if i == tmpsum - n:
                continue
            print(i)


if __name__ == "__main__":
    main()

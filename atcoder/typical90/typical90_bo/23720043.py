#!/usr/bin/env python3
def base10int(value, base):
    if (int(value // base)):
        return base10int(int(value // base), base) + str(value % base)
    return str(value % base)


def main():
    n, k = map(int, input().split())
    for _ in range(k):
        n = int(str(n), 8)
        n = base10int(n, 9)
        n = n.replace('8', '5')
    print(n)


if __name__ == "__main__":
    main()

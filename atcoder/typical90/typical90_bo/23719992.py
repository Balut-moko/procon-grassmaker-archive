#!/usr/bin/env python3
def base10nine(value):
    if (int(value // 9)):
        return base10nine(int(value // 9)) + str(value % 9)
    return str(value % 9)


def main():
    n, k = map(int, input().split())
    if n == 0:
        exit(print(0))
    for _ in range(k):
        n = int(str(n), 8)
        n = base10nine(n)
        c = ''
        for j in range(len(n)):
            if n[j] == '8':
                c += '5'
            else:
                c += n[j]
        n = int(c)
    print(n)


if __name__ == "__main__":
    main()

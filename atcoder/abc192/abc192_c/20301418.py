#!/usr/bin/env python3
def g1func(n):
    n = sorted(str(n), reverse=True)
    res = int(''.join(n))
    return res


def g2func(n):
    n = sorted(str(n))
    res = int(''.join(n))
    return res


def main():
    n, k = map(int, input().split())
    a = [0] * (k + 1)
    a[0] = n
    for i in range(k):
        a[i + 1] = g1func(a[i]) - g2func(a[i])

    print(a[k])


if __name__ == "__main__":
    main()

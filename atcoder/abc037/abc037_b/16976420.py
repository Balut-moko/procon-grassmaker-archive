#!/usr/bin/env python3

def main():
    n, q = map(int, input().split())
    lrt = [list(map(int, input().split())) for i in range(q)]
    a = [0] * n
    for i in range(q):
        for j in range(lrt[i][0] - 1, lrt[i][1]):
            a[j] = lrt[i][2]
    print(*a, sep='\n')


if __name__ == "__main__":
    main()

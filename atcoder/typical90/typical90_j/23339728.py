#!/usr/bin/env python3

def main():
    n = int(input())
    cumsum = [[0, 0, 0]]
    for i in range(n):
        c, p = map(int, input().split())
        if c == 1:
            cumsum.append([i + 1, cumsum[i][1] + p, cumsum[i][2]])
        else:
            cumsum.append([i + 1, cumsum[i][1], cumsum[i][2] + p])
    q = int(input())
    for j in range(q):
        l, r = map(int, input().split())
        one = cumsum[r][1] - cumsum[l - 1][1]
        two = cumsum[r][2] - cumsum[l - 1][2]
        print(one, two)


if __name__ == "__main__":
    main()

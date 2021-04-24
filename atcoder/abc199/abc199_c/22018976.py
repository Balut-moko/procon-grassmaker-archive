#!/usr/bin/env python3

def main():
    n = int(input())
    s = list(input())
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    tmp = True
    for i in range(q):
        if query[i][0] == 1:
            if tmp:
                a = query[i][1] - 1
                b = query[i][2] - 1
            else:
                a = ((query[i][1] + n) % (2 * n)) - 1
                b = ((query[i][2] + n) % (2 * n)) - 1
            s[a], s[b] = s[b], s[a]
        else:
            tmp = not tmp
    if not tmp:
        s = s[n:] + s[:n]
    print(*s, sep='')


if __name__ == "__main__":
    main()

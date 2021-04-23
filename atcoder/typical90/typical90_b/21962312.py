#!/usr/bin/env python3
def check(S):
    cnt = 0
    for s in S:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    return False


def main():
    n = int(input())
    if n % 2 == 1:
        print()
        return
    for i in range(1 << n):
        S = ''
        for j in range(n - 1, -1, -1):
            if (i >> j) & 1 == 0:
                S += '('
            else:
                S += ')'
        if check(S):
            print(S)


if __name__ == "__main__":
    main()

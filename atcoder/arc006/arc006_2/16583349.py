#!/usr/bin/env python3

def main():
    n, ln = map(int, input().split())

    s = [" " + input() + " " for i in range(ln + 1)]
    ans = s[ln].index('o')
    for i in reversed(range(ln)):
        if s[i][ans - 1] == '-':
            ans -= 2
        elif s[i][ans + 1] == '-':
            ans += 2

    print(ans // 2 + 1)


if __name__ == "__main__":
    main()

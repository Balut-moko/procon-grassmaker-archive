#!/usr/bin/env python3
import collections


def main():
    S = input()
    T = int(input())
    cnt = collections.Counter(S)
    x = cnt['R'] - cnt['L']
    y = cnt['U'] - cnt['D']
    ans = abs(x) + abs(y)
    if T == 1:
        ans += cnt['?']
    else:
        if ans >= cnt['?']:
            ans -= cnt['?']
        else:
            ans = (cnt['?'] - ans) % 2
    print(ans)


if __name__ == "__main__":
    main()

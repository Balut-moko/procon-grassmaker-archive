#!/usr/bin/env python3
import collections


def main():
    N = int(input())
    S = input()
    RGB = ('R', 'G', 'B')
    cnt = collections.Counter(S)
    ans = cnt['R'] * cnt['G'] * cnt['B']

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if S[i] != S[j]:
                if 2 * j - i < N:
                    if S[2 * j - i] == RGB[3 - RGB.index(S[i]) - RGB.index(S[j])]:
                        ans -= 1

    print(ans)


if __name__ == "__main__":
    main()

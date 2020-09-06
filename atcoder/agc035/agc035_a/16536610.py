#!/usr/bin/env python3
import collections


def main():
    n = int(input())
    a = list(map(int, input().split()))

    c = collections.Counter(a).most_common()
    ans = "No"
    if len(c) == 3 and c[0][1] == c[1][1] == c[2][1]:
        if c[0][0] ^ c[1][0] ^ c[2][0] == 0:
            ans = "Yes"
    elif len(c) == 2 and c[0][1] == 2 * c[1][1]:
        if c[0][0] ^ c[0][0] ^ c[1][0] == 0:
            ans = "Yes"
    elif len(c) == 1 and c[0][0] == 0:
        ans = "Yes"
    print(ans)


if __name__ == "__main__":
    main()

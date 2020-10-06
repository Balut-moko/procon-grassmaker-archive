#!/usr/bin/env python3
import collections


def main():
    s = input()
    cnt = collections.Counter(s)
    ans = 'YES'
    if cnt.most_common()[0][1] > (len(s)-1) // 3 + 1:
        ans = 'NO'
    print(ans)


if __name__ == "__main__":
    main()

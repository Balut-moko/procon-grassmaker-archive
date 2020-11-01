#!/usr/bin/env python3
import collections
import itertools


def main():
    s = input()
    cnt = collections.Counter(s)
    numlist = []
    ans = 'No'
    if cnt['8'] >= 3:
        ans = 'Yes'
    else:
        for i in range(10):
            for _ in range(1, min(3, cnt[str(i)] + 1)):
                numlist.append(str(i))
        for v in itertools.permutations(numlist):
            num = int("".join(v))
            if num % 8 == 0:
                ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()

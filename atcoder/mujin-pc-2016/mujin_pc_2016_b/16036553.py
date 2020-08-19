#!/usr/bin/env python3
import math


def main():
    la, lb, lc = map(int, input().split())
    ans = math.pi*(la+lb+lc)**2
    if la > lb + lc:
        ans -= math.pi*(la-lb-lc)**2
    elif lb > la + lc:
        ans -= math.pi*(lb-la-lc)**2
    elif lc > la + lb:
        ans -= math.pi*(lc-la-lb)**2

    print(ans)


if __name__ == "__main__":
    main()

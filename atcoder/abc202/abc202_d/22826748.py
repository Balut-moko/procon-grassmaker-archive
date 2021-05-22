#!/usr/bin/env python3
import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    a, b, k = map(int, input().split())
    n = a + b
    ans = ''
    tmp_num = 0
    b_tmp = b
    while len(ans) < a + b:
        if n == b_tmp:
            ans += 'b' * b_tmp
            break
        tmp = combinations_count(n - 1, b_tmp)
        if tmp + tmp_num < k:
            tmp_num += tmp
            n -= 1
            b_tmp -= 1
            ans += 'b'
        else:
            ans += 'a'
            n -= 1
            if n == 1:
                if b_tmp == 1:
                    ans += 'b'
                else:
                    ans += 'a'
                break
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import itertools


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    s, p = map(int, input().split())
    p_divisors = make_divisors(p)
    ans = 'No'
    for i in range(len(p_divisors) // 2 + 1):
        if p_divisors[i] + p_divisors[len(p_divisors) - i - 1] == s:
            ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()

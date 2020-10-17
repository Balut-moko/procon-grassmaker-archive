#!/usr/bin/env python3


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
    n = int(input())
    div_list = make_divisors(n)
    print(*div_list, sep='\n')


if __name__ == "__main__":
    main()

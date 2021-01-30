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
    if n == 1:
        print(2)
    else:
        li = make_divisors(n)
        li2 = [val for val in li if val % 2 == 1]
        print(len(li2) * 2)


if __name__ == "__main__":
    main()

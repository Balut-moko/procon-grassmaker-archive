#!/usr/bin/env python3
import itertools


def main():
    n = int(input())
    password = list(itertools.product('abc', repeat=n))
    for i in range(len(password)):
        print("".join(password[i]))


if __name__ == "__main__":
    main()

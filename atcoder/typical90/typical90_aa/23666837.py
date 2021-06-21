#!/usr/bin/env python3

def main():
    n = int(input())
    user_set = set()
    for i in range(n):
        s = input()
        if s not in user_set:
            user_set.add(s)
            print(i + 1)


if __name__ == "__main__":
    main()

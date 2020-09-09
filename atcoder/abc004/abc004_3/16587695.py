#!/usr/bin/env python3

def main():
    n = int(input())
    n %= 30
    num = ["1", "2", "3", "4", "5", "6"]
    for i in range(n):
        num[i % 5], num[i % 5 + 1] = num[i % 5 + 1], num[i % 5]
    print("".join(num))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    a = list(input())
    b = list(input()) + [""]
    for i in range(len(a)):
        print(a[i], end="")
        print(b[i], end="")


if __name__ == "__main__":
    main()

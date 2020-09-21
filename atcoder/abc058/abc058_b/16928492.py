#!/usr/bin/env python3

def main():
    a = input()
    b = input()
    for i in range(len(a)):
        print(a[i], end="")
        if i < len(b):
            print(b[i], end="")
    print()


if __name__ == "__main__":
    main()

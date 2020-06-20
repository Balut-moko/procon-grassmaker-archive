#!/usr/bin/env python3

def main():
    X = int(input())
    i = 1
    while True:
        if (X * i) % 360 == 0:
            break
        i += 1
    print(i)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    ab = int(input().replace(" ", ""))
    print("Yes" if int(ab**.5)**2 == ab else "No")


if __name__ == "__main__":
    main()

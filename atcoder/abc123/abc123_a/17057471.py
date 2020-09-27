#!/usr/bin/env python3

def main():
    antenna = [int(input()) for i in range(5)]
    k = int(input())
    print(":(" if max(antenna) - min(antenna) > k else "Yay!")


if __name__ == "__main__":
    main()

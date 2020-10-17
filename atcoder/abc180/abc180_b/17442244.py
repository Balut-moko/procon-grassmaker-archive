#!/usr/bin/env python3

def main():
    n = int(input())
    X = list(map(int, input().split()))
    X1 = [abs(x) for x in X]
    X2 = [abs(x)**2 for x in X]
    print(sum(X1))
    print(sum(X2)**.5)
    print(max(X1))


if __name__ == "__main__":
    main()

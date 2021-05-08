#!/usr/bin/env python3

def main():
    n, K = map(int, input().split())
    for k in range(K):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + '200')
    print(n)


if __name__ == "__main__":
    main()

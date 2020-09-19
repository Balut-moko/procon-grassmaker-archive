#!/usr/bin/env python3

def main():
    n = int(input())
    li = [1] * (n + 1)
    for i in range(2, n + 1):
        j = 1
        while i * j <= n:
            li[i * j] += 1
            j += 1

    print(sum(li[1:n]))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    n = int(input())
    A = sorted(map(int, input().split()))
    min_a = A[0]
    while True:
        A = [a % min_a for a in A if a % min_a != 0] + [min_a]
        if len(A) == 1:
            break
        else:
            min_a = min(A)
    print(min_a)


if __name__ == "__main__":
    main()

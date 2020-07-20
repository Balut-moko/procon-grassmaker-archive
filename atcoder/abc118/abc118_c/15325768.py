from functools import reduce
import math


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = gcd_list(A)
    print(ans)


if __name__ == "__main__":
    main()
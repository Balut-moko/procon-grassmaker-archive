import math


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(math.ceil(sum(a) / (n - a.count(0))))


if __name__ == "__main__":
    main()

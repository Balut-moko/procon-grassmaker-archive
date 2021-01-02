#!/usr/bin/env python3

def main():
    a, b = input().split()
    sum_a = 0
    sum_b = 0
    for i in range(3):
        sum_a += int(a[i])
        sum_b += int(b[i])
    if sum_a >= sum_b:
        ans = sum_a
    else:
        ans = sum_b
    print(ans)


if __name__ == "__main__":
    main()

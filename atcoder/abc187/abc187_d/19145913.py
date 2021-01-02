#!/usr/bin/env python3

def main():
    n = int(input())
    ab_list = []
    sum_a = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum_a += a
        ab_list.append([a, b, a * 2 + b])
    ab_list = sorted(ab_list, reverse=True, key=lambda x: x[2])

    sum_b = 0
    ans = 0
    for ab in ab_list:
        sum_a -= ab[0]
        sum_b += ab[0] + ab[1]
        ans += 1
        if sum_a < sum_b:
            break
    print(ans)


if __name__ == "__main__":
    main()

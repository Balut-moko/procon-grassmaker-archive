#!/usr/bin/env python3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    num_list = list(range(200001))
    tmp_min = 0
    ans = [0] * n
    for i in range(n):
        num_list[p[i]] = -1
        j = tmp_min
        while num_list[j] != j:
            j += 1
            tmp_min += 1
        ans[i] = j
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()

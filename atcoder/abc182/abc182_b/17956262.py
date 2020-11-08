#!/usr/bin/env python3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    tmp = 0
    for i in range(2, 1001):
        cnt = 0
        for a in A:
            if a % i == 0:
                cnt += 1
        tmp = max(tmp, cnt)
        if tmp == cnt:
            ans = i
    print(ans)


if __name__ == "__main__":
    main()

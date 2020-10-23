#!/usr/bin/env python3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 'DENIED'
    cnt1 = 0
    cnt2 = 0
    for a in A:
        if a % 2 == 0:
            cnt1 += 1
            if a % 3 == 0 or a % 5 == 0:
                cnt2 += 1
    print('APPROVED' if cnt1 == cnt2 else 'DENIED')


if __name__ == "__main__":
    main()

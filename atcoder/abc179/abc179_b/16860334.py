#!/usr/bin/env python3

def main():
    n = int(input())
    cnt = 0
    ans = 'No'
    for i in range(n):
        a, b = map(int, input().split())
        if a == b:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()

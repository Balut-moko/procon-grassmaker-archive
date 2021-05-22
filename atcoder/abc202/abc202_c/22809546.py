#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [''] + list(map(int, input().split()))
    c = [''] + list(map(int, input().split()))
    cnt = [0] * (n + 1)
    ans = 0
    for j in range(1, n + 1):
        cnt[b[c[j]]] += 1
    for i in range(n):
        ans += cnt[a[i]]

    print(ans)


if __name__ == "__main__":
    main()

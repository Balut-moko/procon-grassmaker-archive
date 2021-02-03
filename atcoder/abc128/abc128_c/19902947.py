#!/usr/bin/env python3

def main():
    n, M = map(int, input().split())
    ks = [list(map(int, input().split())) for i in range(M)]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        tmp = 0
        for m in range(M):
            cnt = 0
            for j in range(ks[m][0]):
                if (i >> (ks[m][j + 1]-1)) & 1:
                    cnt += 1
            if cnt % 2 == p[m]:
                tmp += 1
        if tmp == M:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()

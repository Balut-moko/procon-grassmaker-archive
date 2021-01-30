#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        dish = [0] * n
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]-1] += 1
            else:
                dish[cd[j][1]-1] += 1
        tmp = 0
        for i in range(m):
            if dish[ab[i][0]-1] * dish[ab[i][1]-1] > 0:
                tmp += 1
        ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()

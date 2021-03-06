#!/usr/bin/env python3

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ans = 10**11
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, ab[i][0] + ab[j][1])
            else:
                ans = min(ans, max(ab[i][0], ab[j][1]))

    print(ans)


if __name__ == "__main__":
    main()

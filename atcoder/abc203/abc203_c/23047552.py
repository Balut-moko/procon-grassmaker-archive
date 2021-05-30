#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab = sorted(ab)
    ans = k
    for i in ab:
        if ans < i[0]:
            break
        else:
            ans += i[1]
    print(ans)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    k, a, b = map(int, input().split())
    if b - a > 2:
        ans = min(k + 1, a)
        k -= a - 1
        if k > 0:
            ans += (k // 2) * (b - a)
            k %= 2
            if k == 1:
                ans += 1
    else:
        ans = k + 1
    print(ans)


if __name__ == "__main__":
    main()

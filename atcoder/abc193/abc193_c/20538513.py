#!/usr/bin/env python3

def main():
    n = int(input())
    ans = set()
    for b in range(2, 32):
        for a in range(2, n // 2 + 1):
            if a**b <= n:
                ans.add(a**b)
            else:
                break
    print(n - len(ans))


if __name__ == "__main__":
    main()

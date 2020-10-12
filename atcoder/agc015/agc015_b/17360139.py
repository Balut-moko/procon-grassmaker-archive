#!/usr/bin/env python3

def main():
    S = input()
    n = len(S)
    ans = 0
    for i in range(n):
        if S[i] == 'U':
            ans += (n - i - 1) * 1 + i * 2
        else:
            ans += (n - i - 1) * 2 + i * 1

    print(ans)


if __name__ == "__main__":
    main()

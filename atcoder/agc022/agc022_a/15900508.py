#!/usr/bin/env python3
import string


def main():
    S = input()
    S_temp = S
    ans_temp = 'zyxwvutsrqponmlkjihgfedcba'
    for i in range(len(S) + 1):
        for c in string.ascii_lowercase:
            if c not in S[:i]:
                S_temp = S[:i] + c
                if S < S_temp:
                    break
        if S < S_temp and S_temp < ans_temp:
            ans_temp = S_temp
    print(ans_temp if S < ans_temp else -1)


if __name__ == "__main__":
    main()

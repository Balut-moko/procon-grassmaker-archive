#!/usr/bin/env python3

def main():
    S = input()
    n = len(S)
    pre = ''
    ans, cnt = 0, 0
    for i in range(1, n):
        if S[i - 1] == S[i] and S[i] != pre:
            if pre != '':
                ans += cnt + n - i
            cnt = 0
            pre = S[i]
        if pre != '' and S[i] != pre:
            cnt += 1
    ans += cnt

    print(ans)


if __name__ == "__main__":
    main()

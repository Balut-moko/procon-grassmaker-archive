#!/usr/bin/env python3

def main():
    s = input()
    t = input()
    ans = 'You can win'
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] == '@' and t[i] in 'atcoder':
                continue
            elif t[i] == '@' and s[i] in 'atcoder':
                continue
            ans = 'You will lose'

    print(ans)


if __name__ == "__main__":
    main()

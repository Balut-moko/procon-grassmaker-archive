#!/usr/bin/env python3

def main():
    S = input()
    flg = True
    t = ''
    for s in S:
        if s == 'R':
            flg = not flg
        else:
            if flg:
                if len(t) > 0 and t[-1] == s:
                    t = t[:-1]
                else:
                    t = t + s
            else:
                if len(t) > 0 and t[0] == s:
                    t = t[1:]
                else:
                    t = s + t
    if not flg:
        t = t[::-1]
    print(t)


if __name__ == "__main__":
    main()

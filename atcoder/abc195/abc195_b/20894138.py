#!/usr/bin/env python3


def main():
    a, b, w = map(int, input().split())
    w *= 1000
    ans = [0, 0]
    flg = True
    i = 1
    while ans[0] == 0:
        tmp_max = b * i
        if w <= tmp_max:
            ans[0] = i
        else:
            i += 1
    j = i
    if w < a * j:
        flg = False
    while ans[1] == 0:
        tmp_min = a * j
        if w < tmp_min:
            ans[1] = j - 1
        else:
            j += 1
    if flg:
        print(*ans)
    else:
        print('UNSATISFIABLE')


if __name__ == "__main__":
    main()

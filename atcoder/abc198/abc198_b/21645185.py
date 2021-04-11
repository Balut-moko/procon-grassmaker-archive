#!/usr/bin/env python3

def main():
    n = input()
    re_n = n[::-1]
    tmp = 0
    for s in re_n:
        if s != '0':
            break
        tmp += 1

    tmp_n = '0' * tmp + n
    i = 0
    j = len(tmp_n) - 1
    ans = 'Yes'
    while i < j:
        if tmp_n[i] != tmp_n[j]:
            ans = 'No'
            break
        i += 1
        j -= 1

    print(ans)


if __name__ == "__main__":
    main()

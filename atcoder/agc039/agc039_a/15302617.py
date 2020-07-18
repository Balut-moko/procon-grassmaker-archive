#!/usr/bin/env python3

def main():
    S = input()
    K = int(input())

    cnt = 0
    ans = 0
    s_temp = S[0]
    fcnt = 0
    for s in S:
        if s_temp == s:
            cnt += 1
            s_temp = s
        else:
            ans += cnt // 2
            if fcnt == 0:
                fcnt = cnt
            cnt = 1
            s_temp = s
    if fcnt == 0:
        fcnt = cnt
    ans += cnt // 2
    ans *= K
    if len(S) == fcnt:
        ans = (len(S) * K) // 2
    elif S[0] == S[-1]:
        ans -= (fcnt // 2 + cnt // 2 - (fcnt + cnt) // 2) * (K - 1)

    print(ans)


if __name__ == "__main__":
    main()

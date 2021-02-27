#!/usr/bin/env python3

def point(card_str):
    res = 0
    for i in range(10):
        res += i * 10 ** card_str.count(str(i))
    return res


def main():
    K = int(input())
    S = input()
    T = input()
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            S_tmp = S.replace('#', str(i))
            T_tmp = T.replace('#', str(j))
            if K < S_tmp.count(str(i)) + T_tmp.count(str(i)):
                continue
            if K < S_tmp.count(str(j)) + T_tmp.count(str(j)):
                continue
            if point(T_tmp) < point(S_tmp):
                ans += (K - S.count(str(i)) - T.count(str(i))) * (K - S_tmp.count(str(j)) - T.count(str(j)))

    print(ans / ((9 * K - 8) * (9 * K - 9)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    S = input()
    ans = 0
    if 4 < S.count('o'):
        print(ans)
        return
    must_num = []
    for i, s in enumerate(S):
        if s == 'o':
            must_num.append(i)
    for i in range(10000):
        tmp = str(i).zfill(4)
        flg = True
        for num in must_num:
            if str(num) not in tmp:
                flg = False
        if not flg:
            continue
        flg = True
        for t in tmp:
            if S[int(t)] == 'x':
                flg = False
        if not flg:
            continue
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()

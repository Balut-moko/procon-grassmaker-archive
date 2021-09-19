from sys import stdin


def make10(bou2, bou3, bou4):
    res = 0
    bou6 = bou3 // 2
    if bou4 <= bou6:
        res += bou4
        bou6 -= bou4
        if bou2 // 2 <= bou6:
            res += bou2 // 2
        else:
            res += bou6
            bou2 -= bou6 * 2
            res += bou2 // 5
    else:
        res += bou6
        bou4 -= bou6
        bou8 = bou4 // 2
        if bou2 <= bou8:
            res += bou2
        else:
            res += bou8
            bou2 -= bou8
            if bou4 % 2 == 1:
                if 3 <= bou2:
                    res += 1
                    bou2 -= 3
            res += bou2 // 5
    return res


readline = stdin.readline
n = int(readline())
for i in range(n):
    bou2, bou3, bou4 = map(int, readline().split())
    print(make10(bou2, bou3, bou4))

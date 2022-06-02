from sys import stdin
from bisect import bisect_left


def calc_arithmetix_number(x):
    li = []
    for i in range(1, 10):
        tmp = str(i)
        if x <= i:
            li.append(i)
        for j in range(-9, 10):
            ii = i
            tmp = str(i)
            while 0 <= ii + j < 10:
                tmp += str(ii + j)
                ii += j
                li.append(int(tmp))
                if x <= int(tmp) or ii == 0:
                    break

    return li


readline = stdin.readline
x = int(readline())
li = calc_arithmetix_number(x)
li.sort()
ans = li[bisect_left(li, x)]
print(ans)

from itertools import permutations
from sys import stdin


def ten2baseint(value, base):
    """
    10進数からn進数へ変換
    """
    if int(value // base):
        return ten2baseint(int(value // base), base) + str(value % base)
    return str(value % base)


readline = stdin.readline
n = int(readline())
num = 0
num_set = set()
while num < (1 << 20):
    num += 1
    str4 = ten2baseint(num, 4)

    if str4.count("0") != 0:
        continue
    if str4.count("1") == 0:
        continue
    if str4.count("2") == 0:
        continue
    if str4.count("3") == 0:
        continue
    num_str = ""
    for v in str4:
        if v == "1":
            num_str += "3"
        if v == "2":
            num_str += "5"
        if v == "3":
            num_str += "7"
    num_set.add(int(num_str))
ans = 0
for val in num_set:
    if val <= n:
        ans += 1
print(ans)

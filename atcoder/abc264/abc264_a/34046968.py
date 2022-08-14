from sys import stdin

readline = stdin.readline
atcoder = "atcoder"
l, r = map(int, readline().split())
print(atcoder[l - 1 : r])

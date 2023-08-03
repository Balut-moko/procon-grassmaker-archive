from sys import stdin

readline = stdin.readline
abc = list(map(int, readline().split()))
abc_i = [[val, i] for i, val in enumerate(abc)]

abc_i.sort()

print(chr(ord("A") + abc_i[1][1]))

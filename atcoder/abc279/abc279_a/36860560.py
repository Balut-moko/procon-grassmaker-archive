from sys import stdin

readline = stdin.readline
s = readline()[:-1]

print(s.count("v") + 2 * s.count("w"))

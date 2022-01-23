from sys import stdin

readline = stdin.readline
s = list(readline()[:-1])
a, b = map(lambda x: int(x) - 1, readline().split())
s[a], s[b] = s[b], s[a]
print(*s, sep="")

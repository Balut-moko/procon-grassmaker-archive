from sys import stdin

readline = stdin.readline
l, r = map(lambda x: int(x) - 1, readline().split())
s = readline()[:-1]
print(s[:l], s[l:r + 1][::-1], s[r + 1:], sep='')

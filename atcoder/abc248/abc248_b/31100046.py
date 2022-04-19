from sys import stdin

readline = stdin.readline
a, b, k = map(int, readline().split())
cnt = 0
while a < b:
    a *= k
    cnt += 1
print(cnt)

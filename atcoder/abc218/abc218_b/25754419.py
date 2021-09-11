from sys import stdin

readline = stdin.readline
p = list(map(int, readline().split()))
ans = ''
for val in p:
    ans += chr(96 + val)
print(ans)

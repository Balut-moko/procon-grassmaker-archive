from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = []
for val in a:
    c.append(val)
for val in b:
    c.append(val)
c.sort()
di = dict()
for i,val in enumerate(c):
    di[val] = i+1

ans_a = [0]*n
ans_b = [0]*m

for i,val in enumerate(a):
    ans_a[i] = di[val]
for i,val in enumerate(b):
    ans_b[i] = di[val]

print(*ans_a)
print(*ans_b)
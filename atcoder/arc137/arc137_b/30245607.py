from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
cnt = sum(a)
a = [val if val == 1 else -1 for val in a]

s = [0]
for val in a:
    s.append(s[-1] + val)

min_ss, max_ss = 0, 0

min_val, max_val = 0, 0
tmp = 0
for val in s:
    if max_val < val:
        max_val = val
    if val < min_val:
        min_val = val
        max_val = min_val
    max_ss = max(max_ss, max_val - min_val)


min_val, max_val = 0, 0
tmp = 0
for val in s:
    if max_val < val:
        max_val = val
        min_val = max_val
    if val < min_val:
        min_val = val
    min_ss = min(min_ss, min_val - max_val)

print(max_ss - min_ss + 1)

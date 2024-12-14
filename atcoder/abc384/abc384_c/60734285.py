from collections import defaultdict


def has_bit(n, i):
    return n & (1 << i) > 0


point = list(map(int, input().split()))

ans = defaultdict(set)

for n in range(1, 1 << 5):
    p = 0
    for i in range(5):
        if has_bit(n, i):
            p += point[i]
    name = ""
    for i in range(5):
        if has_bit(n, i):
            name += chr(ord("A") + i)
    ans[p].add(name)


for k, v in sorted(ans.items(), reverse=True):
    for name in sorted(v):
        print(name, sep="")

from collections import Counter
from sys import stdin


def split_str(s: str, length):
    li = []
    prev = 0
    for i in range(length, len(s), length):
        li.append(s[prev:i])
        prev = i
    li.append(s[prev:])
    return li


readline = stdin.readline
n, k = map(int, readline().split())
s = readline()[:-1]
if s.count(s[0]) == n:
    print(1)
    exit()
for i in range(1, n):
    if n % i == 0:
        tmp = 0
        li = list(zip(*split_str(s, i)))
        for val in li:
            c = Counter(val)
            tmp += sum(c.values()) - c.most_common(1)[0][1]
        if tmp <= k:
            print(i)
            exit()
print(n)

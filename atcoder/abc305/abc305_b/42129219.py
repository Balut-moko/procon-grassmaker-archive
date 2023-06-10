from sys import stdin

readline = stdin.readline
p, q = readline().split()
li = [0, 3, 4, 8, 9, 14, 23]
if p > q:
    p, q = q, p

print(li[ord(q) - ord("A")] - li[ord(p) - ord("A")])

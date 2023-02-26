from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

p = [0, 0]
dd = ((1, 0), (-1, 0), (0, 1), (0, -1))
p_set = set()
p_set.add((0, 0))
flag = False
for val in s:
    if val == "R":
        i = 0
    if val == "L":
        i = 1
    if val == "U":
        i = 2
    if val == "D":
        i = 3
    p[0] += dd[i][0]
    p[1] += dd[i][1]
    p_t = tuple(p)
    if p_t in p_set:
        flag = True
    p_set.add(p_t)
print("Yes" if flag else "No")

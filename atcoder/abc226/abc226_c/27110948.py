from sys import stdin

readline = stdin.readline
n = int(readline())
t_li = []
a_set_dict = dict()
for i in range(n):
    t, _, *a = map(lambda x: int(x) - 1, readline().split())
    t_li.append(t + 1)
    a_set_dict[i] = a
waza_set = set()
waza_set.add(n - 1)
for i in range(n - 1, -1, -1):
    if i in waza_set:
        for val in a_set_dict[i]:
            waza_set.add(val)

ans = 0
for i in range(n):
    if i in waza_set:
        ans += t_li[i]
print(ans)

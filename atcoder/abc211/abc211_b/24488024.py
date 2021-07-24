from sys import stdin

readline = stdin.readline
a = [readline()[:-1] for _ in [0] * 4]
hit_set = {'H', '2B', '3B', 'HR'}
for val in a:
    hit_set.discard(val)
if len(hit_set):
    ans = 'No'
else:
    ans = 'Yes'
print(ans)

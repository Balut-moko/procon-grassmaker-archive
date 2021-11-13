from sys import stdin

readline = stdin.readline
n = int(readline())
s = list(map(int, readline().split()))
area = set()
for a in range(1, 200):
    for b in range(1, 200):
        area.add(4 * a * b + 3 * a + 3 * b)

ans = 0
for val in s:
    if val not in area:
        ans += 1
print(ans)

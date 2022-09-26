from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())

test = [False, False, False]

if a >= 4:
    test[2] = True
    a -= 4
if a >= 2:
    test[1] = True
    a -= 2
if a >= 1:
    test[0] = True
if b >= 4:
    test[2] = True
    b -= 4
if b >= 2:
    test[1] = True
    b -= 2
if b >= 1:
    test[0] = True
ans = 0
for i in range(3):
    if test[i]:
        ans += 2 ** i
print(ans)

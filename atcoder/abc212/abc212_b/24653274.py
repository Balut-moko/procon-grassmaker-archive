from sys import stdin

readline = stdin.readline
x = readline()[:-1]
ans = 'Strong'
if x[0] == x[1] == x[2] == x[3]:
    ans = 'Weak'
for i in range(3):
    if (int(x[i]) + 1) % 10 != int(x[i + 1]):
        break
else:
    ans = 'Weak'

print(ans)

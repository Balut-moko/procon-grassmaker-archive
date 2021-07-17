from sys import stdin

readline = stdin.readline
n = int(readline())
S = readline()[:-1]
for i, s in enumerate(S):
    if s == '1':
        if i % 2 == 0:
            ans = 'Takahashi'
        else:
            ans = 'Aoki'
        break
print(ans)

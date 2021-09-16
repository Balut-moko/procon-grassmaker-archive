from sys import stdin

readline = stdin.readline
n = int(readline())
w = [readline()[:-1] for _ in [0] * n]
tmp = w[0][0]
w_set = set()
ans = 'DRAW'
for i in range(n):
    if tmp == w[i][0] and w[i] not in w_set:
        tmp = w[i][-1]
        w_set.add(w[i])
        continue
    else:
        if i % 2 == 0:
            ans = 'LOSE'
        else:
            ans = 'WIN'
        break
print(ans)

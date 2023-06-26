from sys import stdin


readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))


def insert(i, j):
    pre = [p[j], p[j + 1]]
    return p[:i] + pre + p[i:j] + p[j + 2 :]


cnt = 0
act = []

for i in range(n):
    if p[i] == i + 1:
        continue
    for j in range(i + 1, n):
        if p[j] == i + 1:
            if j < n - 1:
                p = insert(i, j)
                cnt += 1
                act.append((j + 1, i))
                break

            p = insert(n - 3, n - 2)
            cnt += 1
            act.append((n - 1, n - 3))
            p = insert(i, n - 2)
            cnt += 1
            act.append((n - 1, i))

flg = True
for i in range(n):
    if p[i] != i + 1:
        flg = False

if cnt > 2000 or not flg:
    print("No")
    exit()
print("Yes")
print(cnt)
for val in act:
    print(*val)

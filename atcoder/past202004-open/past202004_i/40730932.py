from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = [0] * (1 << n)
que = [(i, v) for i, v in enumerate(a)]
que2 = []
cnt = 1
while len(que) > 1:
    while len(que) > 1:
        ri, rv = que.pop()
        li, lv = que.pop()
        ans[ri] = cnt
        ans[li] = cnt
        if rv < lv:
            que2.append((li, lv))
        else:
            que2.append((ri, rv))
    cnt += 1
    que, que2 = que2, []

print(*ans, sep="\n")

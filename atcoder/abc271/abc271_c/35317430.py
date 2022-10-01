from collections import Counter, deque
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
cnt = Counter(a)
tmp = 0
for key,val in cnt.items():
    tmp += val -1
    cnt[key] = 1
cnt[10**10] = tmp
que = deque(sorted(cnt.items()))

ans = 0
while que:
    key, val = que.popleft()
    if ans +1 == key:
        ans +=1
        val -= 1
        if val > 0:
            que.append((key,val))
        continue
    que.appendleft((key,val))
    key2,val2 = que.pop()
    if val2 >= 2:
        val2 -= 2
        ans += 1
        if val2 > 0:
            que.append((key2,val2))
        continue
    if val2 == 1:
        if que:
            key3,val3 = que.pop()
            val3 -= 1
            ans += 1
            if val3 > 0:
                que.append((key3,val3))
            continue
print(ans)
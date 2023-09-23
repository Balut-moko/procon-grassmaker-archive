n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = -1
for i in range(101):
    tmp = a + [i]
    tmp.sort()
    score = sum(tmp) - tmp[0] - tmp[-1]
    if x <= score:
        ans = i
        break
print(ans)

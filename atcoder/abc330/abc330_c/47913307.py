from bisect import bisect_left


D = int(input())

yy_lst = [i * i for i in range(2 * 10**6 + 1)]
ans = D
for x in range(2 * 10**6 + 1):
    if D < x * x:
        break
    tmp = D - x * x
    idx = bisect_left(yy_lst, tmp)
    yy = yy_lst[idx]
    ans = min(ans, abs(x * x + yy - D))
    yy = yy_lst[idx - 1]
    ans = min(ans, abs(x * x + yy - D))

print(ans)

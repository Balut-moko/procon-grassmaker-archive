from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
cnt_4, cnt_not4, cnt_2 = 0, 0, 0
for val in a:
    if val % 4 == 0:
        cnt_4 += 1
    elif val % 2 == 0:
        cnt_2 += 1
    else:
        cnt_not4 += 1
if n // 2 <= cnt_4:
    ans = 'Yes'
elif (n - cnt_2 + 1) // 2 <= cnt_4:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)

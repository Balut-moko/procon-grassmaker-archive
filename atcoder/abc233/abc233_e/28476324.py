from sys import stdin
readline = stdin.readline
x = list(map(int, readline()[:-1]))
digit = len(x)
ans = []
sum_digit = sum(x)
cnt = 0
for i in range(digit):
    cnt += sum_digit
    ans.append(cnt % 10)
    cnt //= 10
    sum_digit -= x[digit - 1 - i]
while cnt != 0:
    cnt += sum_digit
    ans.append(cnt % 10)
    cnt //= 10
print(*ans[::-1], sep='')

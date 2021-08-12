from sys import stdin

readline = stdin.readline
n = int(readline())
t = readline()[:-1]
tmp = ''
ans = 0
if t == '1':
  ans = (10**10) * 2
elif t == '11':
  ans = 10**10
else:
  zero_cnt = t.count('0')
  for i in range(1,n//3+3):
    tmp += '110'
    if t in tmp:
      ans = 10**10 - zero_cnt
      if t[-1] == '0':
        ans += 1
      break

print(ans)

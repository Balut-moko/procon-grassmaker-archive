from sys import stdin

readline = stdin.readline
m = int(readline())
if m < 100:
  vv = '00'
elif 100 <= m <= 5000:
  vv = m//100
  if vv < 10:
    vv = '0' + str(vv)
elif 6000 <= m <= 30000:
  vv = m//1000 + 50
elif 35000 <= m <= 70000:
  vv = (m//1000 - 30) // 5 + 80
elif 70000 < m:
  vv = 89
print(vv)
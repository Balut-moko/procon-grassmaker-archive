from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = 'oxxoxxoxxoxxoxxoxxoxxoxxoxxoxx'
if s in t:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)

from sys import stdin

readline = stdin.readline
s = readline()[:-1]
flg = True
if len(s) != 8:
    print("No")
    exit()

if not s[0].isupper():
    flg = False
if not s[7].isupper():
    flg = False
try:
    num = int(s[1:7])
except:
    num = 0
if not 100000 <= num <= 999999:
    flg = False
print("Yes" if flg else "No")

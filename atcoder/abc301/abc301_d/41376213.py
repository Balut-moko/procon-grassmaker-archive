from sys import stdin

readline = stdin.readline
s = readline()[:-1]
n = int(readline())
digit = len(s) - 1
num = 0

ss = s.replace("?", "0")
digit_ss = len(ss) - 1
for val in ss:
    if val == "1":
        num += 2 ** digit_ss
    digit_ss -= 1

for val in s:
    if val == "?":
        if num + 2 ** digit <= n:
            num += 2 ** digit
        else:
            pass
    digit -= 1

if n < num:
    print(-1)
else:
    print(num)

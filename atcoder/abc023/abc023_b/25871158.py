from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
acs = 'b'
for i in range(1, 51):
    if acs == s:
        print(i - 1)
        exit()
    if i % 3 == 1:
        acs = 'a' + acs + 'c'
    elif i % 3 == 2:
        acs = 'c' + acs + 'a'
    else:
        acs = 'b' + acs + 'b'


print(-1)

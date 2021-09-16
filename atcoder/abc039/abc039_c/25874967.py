from sys import stdin

readline = stdin.readline
s = readline()[:-1]
doremi = ['Do', '', 'Re', '', 'Mi', 'Fa', '', 'So', '', 'La', '', 'Si']
for i in range(20):
    if s[i] == 'W' and s[i + 1] == 'W':
        if s[i + 6] == 'W':
            ans = doremi[1 - i]
        else:
            ans = doremi[4 - i]
            break
print(ans)

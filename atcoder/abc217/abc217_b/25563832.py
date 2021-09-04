from sys import stdin

readline = stdin.readline
con_set = {'ABC', 'ARC', 'AGC', 'AHC'}
for i in range(3):
    con_set.remove(readline()[:-1])

print(con_set.pop())

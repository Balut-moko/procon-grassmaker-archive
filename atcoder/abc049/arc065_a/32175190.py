from sys import stdin

readline = stdin.readline
s = readline()[:-1]


s = s.replace("eraser", "_")
s = s.replace("erase", "_")
s = s.replace("dreamer", "_")
s = s.replace("dream", "_")

if s.count("_") == len(s):
    ans = "YES"
else:
    ans = "NO"
print(ans)

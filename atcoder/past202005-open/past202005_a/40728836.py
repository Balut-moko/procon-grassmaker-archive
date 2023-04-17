from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]
if s == t:
    ans = "same"
elif s.lower() == t.lower():
    ans = "case-insensitive"
else:
    ans = "different"
print(ans)

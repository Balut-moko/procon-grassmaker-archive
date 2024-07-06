a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
# max(a,c)≤min(b,d)
flag = True
if max(a, g) >= min(d, j):
    flag = False
if max(b, h) >= min(e, k):
    flag = False
if max(c, i) >= min(f, l):
    flag = False

print("Yes" if flag else "No")

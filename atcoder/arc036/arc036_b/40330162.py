from sys import stdin

readline = stdin.readline
n = int(readline())
h = [int(readline()) for _ in [0] * n]
s, t, u = 0, 0, 0
now = 0
st = dict()
for i in range(n):
    if now < h[i]:
        now = h[i]
    else:
        st[s] = i - 1
        s = i
        now = h[i]
st[s] = n - 1

tu = dict()
for i in range(n):
    if h[i] < now:
        now = h[i]
    else:
        tu[t] = i - 1
        t = i
        now = h[i]
tu[t] = n - 1
ans = 1
for s, t in st.items():
    if t in tu.keys():
        u = tu[t]
        ans = max(ans, u - s + 1)
print(ans)

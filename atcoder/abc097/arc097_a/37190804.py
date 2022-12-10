from sys import stdin

readline = stdin.readline
s = readline()[:-1]
k = int(readline())
st = set()
for i in range(k):
    for j in range(len(s) - i):
        st.add(s[j : i + j + 1])
ans = sorted(st)[k - 1]
print(ans)

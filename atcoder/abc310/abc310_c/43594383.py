from sys import stdin

readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]

ans = set()

for i in range(n):
    ward = s[i]
    if s[i] > s[i][::-1]:
        ward = s[i][::-1]
    ans.add(ward)
print(len(ans))

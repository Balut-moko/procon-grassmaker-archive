from string import ascii_uppercase


S = input()
dic = dict()

for i, s in enumerate(S):
    dic[s] = i

cur = dic["A"]
ans = 0
for c in ascii_uppercase:
    ans += abs(cur - dic[c])
    cur = dic[c]

print(ans)

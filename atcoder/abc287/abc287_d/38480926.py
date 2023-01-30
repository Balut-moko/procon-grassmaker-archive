from sys import stdin

readline = stdin.readline
s = list(readline()[:-1])
t = list(readline()[:-1])
len_t = len(t)
ss = s[-len_t:]
flags = [True] * len_t
flag_cnt = 0
for i in range(len_t):
    if ss[i] == "?" or t[i] == "?":
        flag_cnt += 1
        continue
    if ss[i] == t[i]:
        flag_cnt += 1
        continue
    flags[i] = False
print("Yes" if flag_cnt == len_t else "No")

for i in range(len_t):
    if s[i] == "?" or t[i] == "?":
        if not flags[i]:
            flag_cnt += 1
        flags[i] = True
    elif s[i] == t[i]:
        if not flags[i]:
            flag_cnt += 1
        flags[i] = True
    else:
        if flags[i]:
            flag_cnt -= 1
        flags[i] = False
    print("Yes" if flag_cnt == len_t else "No")

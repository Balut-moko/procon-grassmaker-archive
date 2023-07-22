from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
cnt = [0] * 3
flag = False
for i in range(n):
    if s[i] == "A":
        cnt[0] += 1
    if s[i] == "B":
        cnt[1] += 1
    if s[i] == "C":
        cnt[2] += 1

    for j in range(3):
        if cnt[j] != 0:
            continue
        break
    else:
        flag = True
    if flag:
        print(i + 1)
        exit()

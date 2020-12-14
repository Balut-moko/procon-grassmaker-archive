num = list(input().split("+"))
cnt = 0
for n in num:
  if not "0" in n:
    cnt += 1
print(cnt)
from sys import stdin

readline = stdin.readline
s = readline()[:-1]

if s[0] == "1":
    print("No")
    exit()

rows = [False] * 7

for i in range(7):
    if i == 0:
        if s[6] == "0":
            rows[i] = True
    if i == 1:
        if s[3] == "0":
            rows[i] = True
    if i == 2:
        if s[1] == "0" and s[7] == "0":
            rows[i] = True
    if i == 3:
        if s[0] == "0" and s[4] == "0":
            rows[i] = True
    if i == 4:
        if s[2] == "0" and s[8] == "0":
            rows[i] = True
    if i == 5:
        if s[5] == "0":
            rows[i] = True
    if i == 6:
        if s[9] == "0":
            rows[i] = True
left = False
right = False
center = False

for row in rows:
    if row == False:
        if left == False:
            left = True
        else:
            if center == True:
                right = True
    if row == True:
        if left == True:
            center = True

if left and right and center:
    ans = "Yes"
else:
    ans = "No"
print(ans)

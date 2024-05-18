A, B, C, D = map(int, input().split())
div, mod = divmod(C - A, 4)
pattern = [div] * 4
As = A % 4
for i in range(mod):
    pattern[(As + i) % 4] += 1

BD = D - B

ans = 0
start = B % 2
div_y, mod_y = divmod(BD, 2)

ans += pattern[0] * 3 * div_y
if pattern[0] and mod_y == 1:
    if start == 0:
        ans += 2 * pattern[0]
    else:
        ans += 1 * pattern[0]

ans += pattern[1] * 3 * div_y
if pattern[1] and mod_y == 1:
    if start == 0:
        ans += 1 * pattern[1]
    else:
        ans += 2 * pattern[1]

ans += pattern[2] * div_y
if pattern[2] and mod_y == 1:
    if start == 0:
        ans += 0
    else:
        ans += 1 * pattern[2]

ans += pattern[3] * div_y
if pattern[3] and mod_y == 1:
    if start == 0:
        ans += 1 * pattern[3]
    else:
        ans += 0

print(ans)

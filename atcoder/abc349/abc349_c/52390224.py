S = input() + "X"
T = input()

i = 0

for s in S:
    if i == 3:
        break
    if s.upper() == T[i]:
        i += 1

print("Yes" if i == 3 else "No")

N = int(input())
S = input()
flag = False
if "ab" in S or "ba" in S:
    flag = True

print("Yes" if flag else "No")

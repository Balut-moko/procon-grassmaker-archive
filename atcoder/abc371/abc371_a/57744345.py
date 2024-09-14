S = input().split()

# AB,AC,BC
if S[0] == "<" and S[1] == "<" and S[2] == "<":
    ans = "B"
if S[0] == "<" and S[1] == "<" and S[2] == ">":
    ans = "C"
if S[0] == "<" and S[1] == ">" and S[2] == "<":
    ans = "C"
if S[0] == "<" and S[1] == ">" and S[2] == ">":
    ans = "A"
if S[0] == ">" and S[1] == "<" and S[2] == "<":
    ans = "A"
if S[0] == ">" and S[1] == "<" and S[2] == ">":
    ans = "C"
if S[0] == ">" and S[1] == ">" and S[2] == "<":
    ans = "C"
if S[0] == ">" and S[1] == ">" and S[2] == ">":
    ans = "B"

print(ans)

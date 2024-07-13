R, G, B = map(int, input().split())
C = input()

if C == "Red":
    ans = min(G, B)
if C == "Green":
    ans = min(R, B)
if C == "Blue":
    ans = min(R, G)

print(ans)

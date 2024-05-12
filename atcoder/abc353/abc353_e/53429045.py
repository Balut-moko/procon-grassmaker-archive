N = int(input())
S = list(input().split())

tree = {}
ans = 0
for s in S:
    current = tree
    for c in s:
        if c in current:
            ans += current[c][0]
            current[c][0] += 1
        else:
            current[c] = [1, {}]
        current = current[c][1]
print(ans)

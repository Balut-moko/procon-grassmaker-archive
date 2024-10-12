from collections import defaultdict
from string import ascii_uppercase


S = input()
right = defaultdict(int)
for s in S:
    right[s] += 1

left = defaultdict(int)
ans = 0
for s in S:
    right[s] -= 1
    for c in ascii_uppercase:
        ans += left[c] * right[c]
    left[s] += 1

print(ans)

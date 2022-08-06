from collections import Counter
from sys import stdin

readline = stdin.readline
card = list(map(int, readline().split()))

cnt = Counter(card)
most_common = cnt.most_common(2)
if most_common[0][1] == 3 and most_common[1][1] == 2:
    ans = "Yes"
else:
    ans = "No"
print(ans)

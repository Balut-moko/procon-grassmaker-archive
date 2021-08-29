from sys import stdin
from collections import Counter
readline = stdin.readline
n = int(readline())
st = Counter([tuple(readline().split()) for _ in [0] * n])
if 1 < st.most_common()[0][1]:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)

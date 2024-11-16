from itertools import groupby


S = input()

ans = [len(list(g)) for k, g in groupby(S) if k == "-"]

print(*ans)

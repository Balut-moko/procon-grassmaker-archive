from sys import stdin

readline = stdin.readline

s = [readline()[:-1] for _ in [0] * 2]
ans = 'Yes'
if (s == ['.#', '#.']) or (s == ['#.', '.#']):
    ans = 'No'
print(ans)

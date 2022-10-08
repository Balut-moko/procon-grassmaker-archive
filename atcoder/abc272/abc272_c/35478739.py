from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_odd = [val for val in a if val % 2 == 1]
a_even = [val for val in a if val % 2 == 0]
a_odd.sort(reverse=True)
a_even.sort(reverse=True)

ans = -1

if len(a_odd) >= 2:
    ans = max(ans, a_odd[0] + a_odd[1])
if len(a_even) >= 2:
    ans = max(ans, a_even[0] + a_even[1])

print(ans)

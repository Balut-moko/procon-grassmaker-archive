from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_set = set(a)
xor_sum = a[0]
cnt = 0
for i in range(1, n):
    xor_sum ^= a[i]
for i in range(n):
    if xor_sum ^ a[i] == 0:
        print('Win')
        exit()
    if xor_sum ^ a[i] not in a_set:
        cnt += 1
if cnt % 2 == 1:
    ans = 'Win'
else:
    ans = 'Lose'
print(ans)

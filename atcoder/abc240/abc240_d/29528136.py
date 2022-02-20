from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

stack = deque([])
balls = 0
for i in range(n):
    if len(stack) > 0 and a[i] == stack[-1][0]:
        stack[-1][1] += 1
    else:
        stack.append([a[i], 1])
    balls += 1
    if len(stack) > 0 and stack[-1][0] == stack[-1][1]:
        _, cnt = stack.pop()
        balls -= cnt
    print(balls)

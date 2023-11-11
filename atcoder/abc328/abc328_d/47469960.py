from collections import deque


S = input()

que = deque(list(S))
ans = deque([])

while que:
    c = que.popleft()
    ans.append(c)
    if len(ans) >= 3:
        if ans[-3] == "A" and ans[-2] == "B" and ans[-1] == "C":
            ans.pop()
            ans.pop()
            ans.pop()

print(*ans, sep="")

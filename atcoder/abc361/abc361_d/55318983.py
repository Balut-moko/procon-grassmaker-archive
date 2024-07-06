from collections import defaultdict, deque


N = int(input())
S = input()
T = input()

if S == T:
    print(0)
    exit()

if S.count("B") != T.count("B"):
    print(-1)
    exit()

que = deque([tuple(S + "..")])  # root
dist = defaultdict(int)
dist[tuple(S)] = 0
while que:
    s = que.popleft()
    d = dist[s]
    s = list(s)
    idx = s.index(".")

    for i in range(N + 1):
        if s[i] != "." and s[i + 1] != ".":
            move = s[i : i + 2]
            nxt = s[:i] + [".", "."] + s[i + 2 :]
            nxt[idx], nxt[idx + 1] = s[i], s[i + 1]
            nxt = tuple(nxt)
            if dist[nxt] > 0:
                continue
            dist[nxt] = d + 1
            que.append(nxt)

ans = dist[tuple(T + "..")]

print(ans if ans != 0 else -1)

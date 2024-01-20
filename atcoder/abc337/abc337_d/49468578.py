from collections import deque


H, W, K = map(int, input().split())
S = [input() for _ in [0] * H]
INF = 1 << 60
ans = INF

for r in range(H):
    cnt_o = 0
    cnt = 0

    q = deque()
    for val in S[r]:
        q.append(val)
        # 追加した要素に応じた処理
        if val == ".":
            cnt += 1
        elif val == "x":
            q.clear()
            cnt = 0
        while q and not (len(q) <= K):
            rm = q.popleft()
            # 取り除いた要素に応じた処理
            if rm == ".":
                cnt -= 1
        if len(q) == K:
            ans = min(ans, cnt)

S = list(zip(*S))

for r in range(W):
    cnt_o = 0
    cnt = 0

    q = deque()
    for val in S[r]:
        q.append(val)
        # 追加した要素に応じた処理
        if val == ".":
            cnt += 1
        elif val == "x":
            q.clear()
            cnt = 0
        while q and not (len(q) <= K):
            rm = q.popleft()
            # 取り除いた要素に応じた処理
            if rm == ".":
                cnt -= 1
        if len(q) == K:
            ans = min(ans, cnt)

print(ans if ans != INF else -1)

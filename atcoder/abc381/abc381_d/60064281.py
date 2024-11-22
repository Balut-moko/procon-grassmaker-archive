from collections import defaultdict, deque


N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N // 2):
    if A[2 * i] == A[2 * i + 1]:
        B.append(A[2 * i])
    else:
        B.append(0)

C = []
for i in range(1, (N + 1) // 2):
    if A[2 * i] == A[2 * i - 1]:
        C.append(A[2 * i])
    else:
        C.append(0)


def solve(B):
    ans = 0
    cnt = defaultdict(int)
    q = deque()
    for val in B:
        q.append(val)
        # 追加した要素に応じた処理
        if val == 0:
            q.clear()
            cnt.clear()
        else:
            cnt[val] += 1
        while q and not (cnt[val] <= 1):  # (満たすべき条件)
            rm = q.popleft()
            # 取り除いた要素に応じた処理
            cnt[rm] -= 1
        # 何らかの処理 右端の要素から左に延ばせる最大の長さ
        ans = max(ans, len(q) * 2)
    return ans


print(max(solve(B), solve(C)))

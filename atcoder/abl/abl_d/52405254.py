from atcoder.segtree import SegTree


N, K = map(int, input().split())

A = [int(input()) for _ in [0] * N]

st = SegTree(max, 0, 1 << 19)

for i in range(N):
    mx = st.prod((max(0, A[i] - K)), min(300001, A[i] + K + 1))
    st.set(A[i], mx + 1)
ans = st.prod(0, 300001)
print(ans)

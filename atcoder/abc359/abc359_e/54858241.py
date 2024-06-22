from atcoder.lazysegtree import LazySegTree

N = int(input())
H = list(map(int, input().split()))

INF = 1 << 63
ID = INF


def op(ele1, ele2):
    return (ele1[0] + ele2[0], ele1[1] + ele2[1])


def mapping(func, ele):
    if func != ID:
        ele = list(ele)
        ele[0] = func * ele[1]
        ele = tuple(ele)
    return ele


def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper


e = (0, 0)
id_ = ID
lst = [(0, 1) for _ in range(N + 1)]
seg = LazySegTree(op, e, mapping, composition, id_, lst)


stack = []


ans = [0] * N
for i in range(N):
    idx = -1
    while stack:
        tmp = stack[-1]
        if H[tmp] >= H[i]:
            idx = tmp
            break
        stack.pop()
    seg.apply(idx + 1, i + 1, H[i])
    pre_full = seg.prod(0, i + 1)

    ans[i] = pre_full[0] + 1
    stack.append(i)
print(*ans)

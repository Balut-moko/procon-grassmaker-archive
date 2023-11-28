N, Q = map(int, input().split())
C = list(map(int, input().split()))
idx_lst = [i for i in range(N)]

box = [set([c]) for c in C]

for i in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    if len(box[a]) < len(box[b]):
        for val in box[a]:
            box[b].add(val)
        print(len(box[b]))
        box[a].clear()
    else:
        for val in box[b]:
            box[a].add(val)
        box[b].clear()
        print(len(box[a]))
        box[a], box[b] = box[b], box[a]

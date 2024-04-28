N = int(input())
A = list(map(int, input().split()))
que = []
for i in range(N):
    que.append(A[i])
    while True:
        if len(que) <= 1:
            break
        if que[-1] != que[-2]:
            break
        a = que.pop()
        que.pop()
        que.append(a + 1)

print(len(que))

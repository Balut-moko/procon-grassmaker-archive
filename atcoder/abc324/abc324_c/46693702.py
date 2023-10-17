N, T2 = input().split()
N = int(N)
T2 = list(T2)
ans = []
for i in range(N):
    T = list(input())
    if len(T) + 1 == len(T2):
        for j in range(len(T)):
            if T[j] != T2[j]:
                T.insert(j, T2[j])
                break
        else:
            T.append(T2[-1])
    elif len(T) == len(T2) + 1:
        for j in range(len(T2)):
            if T[j] != T2[j]:
                T.pop(j)
                break
        else:
            T.pop(-1)
    elif len(T) == len(T2):
        for j in range(len(T)):
            if T[j] != T2[j]:
                T[j] = T2[j]
                break

    if T2 == T:
        ans.append(i + 1)

print(len(ans))
print(*ans)

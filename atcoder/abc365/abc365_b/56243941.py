N = int(input())
A = list(map(int, input().split()))

second = sorted(A)[-2]
print(A.index(second) + 1)

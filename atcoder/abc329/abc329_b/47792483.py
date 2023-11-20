N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
AA = [a for a in A if a != max_A]
print(max(AA))

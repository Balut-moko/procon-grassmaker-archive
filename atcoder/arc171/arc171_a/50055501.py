def check(N, A, B):
    if N < A:
        return False
    if min(N - A, (N + 1) // 2) * (N - A) < B:
        return False
    return True


T = int(input())

for _ in range(T):
    N, A, B = map(int, input().split())
    print("Yes" if check(N, A, B) else "No")

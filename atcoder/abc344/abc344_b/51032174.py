ans = []
while True:
    N = int(input())
    ans.append(N)
    if N == 0:
        break

print(*ans[::-1], sep="\n")

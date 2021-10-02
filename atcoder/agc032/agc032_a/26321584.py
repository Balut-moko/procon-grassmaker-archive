from sys import stdin

readline = stdin.readline
n = int(readline())
b = list(map(int, readline().split()))
ans = []
while b:
    for i in range(len(b) - 1, -1, -1):
        if b[i] == i + 1:
            ans.append(b.pop(i))
            break
    else:
        print(-1)
        exit()
print(*ans[::-1], sep='\n')

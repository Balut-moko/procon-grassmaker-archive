H = int(input())

cur = 0

for i in range(60):
    cur += 2**i
    if H < cur:
        print(i + 1)
        break

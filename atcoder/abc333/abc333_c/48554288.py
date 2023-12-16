N = int(input())

s = set()

for i in range(1, 13):
    for j in range(1, 13):
        for k in range(1, 13):
            num = int("1" * i) + int("1" * j) + int("1" * k)
            s.add(num)
li = sorted(s)
print(li[N - 1])

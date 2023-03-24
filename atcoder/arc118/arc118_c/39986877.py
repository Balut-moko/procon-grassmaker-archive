from sys import stdin

readline = stdin.readline
n = int(readline())
init_li = [6, 10, 15]

ans_s = set(init_li)
n -= 3
li = [6 * i for i in range(2, 1667)]
while n and li:
    val = li.pop()
    if val not in ans_s:
        ans_s.add(val)
        n -= 1
li = [10 * i for i in range(2, 1000)]
i = 0
while n and li:
    val = li.pop()
    if val not in ans_s:
        ans_s.add(val)
        n -= 1
li = [15 * i for i in range(2, 667)]
i = 0
while n and li:
    val = li.pop()
    if val not in ans_s:
        ans_s.add(val)
        n -= 1
print(*list(ans_s))

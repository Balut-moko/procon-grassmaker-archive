T = int(input())

for _ in range(T):
    S = input()
    if "atcoder" < S:
        print(0)
        continue

    if S.count("a") == len(S):
        print(-1)
        continue
    for i, val in enumerate(S):
        if val != "a":
            if ord(val) <= ord("t"):
                print(i)
                break
            else:
                print(i - 1)
                break

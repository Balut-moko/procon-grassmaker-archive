def dfs(pattern, turn):
    for i in range(0, 9, 3):
        if pattern[i] == pattern[i + 1] == pattern[i + 2]:
            if pattern[i] != -1:
                return pattern[i]
    for i in range(3):
        if pattern[i] == pattern[i + 3] == pattern[i + 6]:
            if pattern[i] != -1:
                return pattern[i]
    if pattern[0] == pattern[4] == pattern[8]:
        if pattern[0] != -1:
            return pattern[0]
    if pattern[2] == pattern[4] == pattern[6]:
        if pattern[2] != -1:
            return pattern[2]

    if -1 not in pattern:
        score = [0] * 2
        for i in range(9):
            score[pattern[i]] += AA[i]
        return 0 if score[0] > score[1] else 1

    for k in range(9):
        if pattern[k] == -1:
            nxt = pattern[:]
            nxt[k] = turn
            if dfs(nxt, turn ^ 1) == turn:
                return turn
    return turn ^ 1


A = [list(map(int, input().split())) for _ in [0] * 3]
AA = A[0] + A[1] + A[2]

print("Takahashi" if dfs([-1] * 9, 0) == 0 else "Aoki")
pass

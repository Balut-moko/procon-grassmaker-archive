from itertools import permutations


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


def contain_palindrome(s):
    for i in range(N - K + 1):
        if is_palindrome(s[i : i + K]):
            return True
    return False


N, K = map(int, input().split())
S = input()
ans = 0
for s in set("".join(s) for s in permutations(S)):
    if not contain_palindrome(s):
        ans += 1
print(ans)

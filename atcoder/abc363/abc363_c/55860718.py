from more_itertools import distinct_permutations


def is_palindrome(s):
    return s == s[::-1]


def contain_palindrome(s):
    for i in range(N - K + 1):
        if is_palindrome(s[i : i + K]):
            return True
    return False


N, K = map(int, input().split())
S = input()
ans = 0
for s in distinct_permutations(S):
    if not contain_palindrome(s):
        ans += 1
print(ans)

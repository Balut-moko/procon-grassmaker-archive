S = input()
upper = sum(s.isupper() for s in S)

if upper > len(S) // 2:
    print(S.upper())
else:
    print(S.lower())

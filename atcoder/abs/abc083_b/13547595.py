def resolve():
    N, a, b = map(int, input().split())
    result = 0
    for i in range(1,N+1):
        digitSum = sum(list(map(int, str(i))))
        if digitSum >= a and digitSum <= b:
            result += i

    print(result)
resolve()
def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    a_cnt = []
    for i in range(N):
        num = a[i]
        cnt = 0
        while num%2 == 0:
            num = num/2
            cnt +=1
        a_cnt.append(cnt)
    print(min(a_cnt))
resolve()
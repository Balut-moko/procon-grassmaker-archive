def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    for k in range(K):
        A_temp=[0]*(N+1)
        for i in range(N):
            A_temp[max(0,i-A[i])]+=1
            if i+A[i]+1<=N-1:
                A_temp[i+A[i]+1]-=1
            
        A[0]=A_temp[0]
        for j in range(1,N):
            A_temp[j]+=A_temp[j-1]
            A[j]=A_temp[j]
        for ai in A:
            if ai != N:
                break
        else:
            break
                
    print(' '.join([str(a) for a in A]))
    
if __name__ == "__main__":
    main()

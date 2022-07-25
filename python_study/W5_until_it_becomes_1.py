N,K=map(int,input().split())

count = 0
while N != 1:
    if(N%K==0):
        N=N/K
        count += 1
        # print("1",count)
    else:
        N-=1
        count += 1
        # print("2",count)
print(count)

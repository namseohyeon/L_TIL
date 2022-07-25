N,K = map(int,input().split())
LIST = []
for i in range(0,N):
    x = int(input())
    LIST.append(x)

LIST.reverse()
coin = 0
for i in LIST:
    if(i<=K):
        # print(K)
        coin+=K//i
        K=K%i
print(coin)
